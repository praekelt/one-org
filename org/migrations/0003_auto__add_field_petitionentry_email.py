# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PetitionEntry.email'
        db.add_column('org_petitionentry', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=64, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PetitionEntry.email'
        db.delete_column('org_petitionentry', 'email')


    models = {
        'org.petitionentry': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'PetitionEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'blank': 'True'}),
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