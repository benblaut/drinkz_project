# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'recipes_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'recipes', ['Ingredient'])

        # Adding model 'Recipes'
        db.create_table(u'recipes_recipes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'recipes', ['Recipes'])

        # Adding M2M table for field ingredients on 'Recipes'
        m2m_table_name = db.shorten_name(u'recipes_recipes_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipes', models.ForeignKey(orm[u'recipes.recipes'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'recipes.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipes_id', 'ingredient_id'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'recipes_ingredient')

        # Deleting model 'Recipes'
        db.delete_table(u'recipes_recipes')

        # Removing M2M table for field ingredients on 'Recipes'
        db.delete_table(db.shorten_name(u'recipes_recipes_ingredients'))


    models = {
        u'recipes.ingredient': {
            'Meta': {'ordering': "['part']", 'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'recipes.recipes': {
            'Meta': {'ordering': "['name']", 'object_name': 'Recipes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipes.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['recipes']