from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.auth import authenticate
from bottles.models import Bottle
from recipes.models import Recipes, Ingredient
from parties.models import Party
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models import ManyToOneRel

class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': ugettext_lazy(
                                "Please log in again, because your session has"
                                " expired.")})
 
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = " "
         
        if username and password:
            self.user_cache = authenticate(username=username,
            password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data

class BottleForm(forms.ModelForm): 
    typ = forms.ChoiceField(widget = forms.Select(), choices = [])
   
    def __init__(self, *args, **kwargs):
        super(BottleForm, self).__init__(*args, **kwargs)
        items = Ingredient.objects.values_list('part', flat=True).distinct()
        self.fields['typ'].choices = [(item, item) for item in items]

    class Meta:
        model = Bottle
        exclude = ['user']

class PartyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)
        self.fields['bar_list'] = forms.ModelMultipleChoiceField(queryset=Bottle.objects.filter(user=self.current_user))
        rel = ManyToOneRel(Bottle, 'id')
        self.fields['bar_list'].widget = RelatedFieldWidgetWrapper(self.fields['bar_list'].widget, rel, self.user_admin_site)

    class Meta:
        model = Party
        exclude = ['host_user']
