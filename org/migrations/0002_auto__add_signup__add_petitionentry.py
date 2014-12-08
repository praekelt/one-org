# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Signup'
        db.create_table('org_signup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('org', ['Signup'])

        # Adding model 'PetitionEntry'
        db.create_table('org_petitionentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('org', ['PetitionEntry'])


    def backwards(self, orm):
        # Deleting model 'Signup'
        db.delete_table('org_signup')

        # Deleting model 'PetitionEntry'
        db.delete_table('org_petitionentry')


    models = {
        'org.petitionentry': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'PetitionEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'org.signup': {
            'Meta': {'ordering': "('email',)", 'object_name': 'Signup'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['org']