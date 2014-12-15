# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'PetitionEntry', fields ['mobile_number']
        db.delete_unique('org_petitionentry', ['mobile_number'])

        # Removing unique constraint on 'PetitionEntry', fields ['email']
        db.delete_unique('org_petitionentry', ['email'])


        # Changing field 'PetitionEntry.email'
        db.alter_column('org_petitionentry', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'PetitionEntry.mobile_number'
        db.alter_column('org_petitionentry', 'mobile_number', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

    def backwards(self, orm):

        # Changing field 'PetitionEntry.email'
        db.alter_column('org_petitionentry', 'email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, null=True))
        # Adding unique constraint on 'PetitionEntry', fields ['email']
        db.create_unique('org_petitionentry', ['email'])


        # Changing field 'PetitionEntry.mobile_number'
        db.alter_column('org_petitionentry', 'mobile_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, null=True))
        # Adding unique constraint on 'PetitionEntry', fields ['mobile_number']
        db.create_unique('org_petitionentry', ['mobile_number'])


    models = {
        'org.petitionentry': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'PetitionEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
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