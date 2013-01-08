# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('contact_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_contact', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nom_contact', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('tel_contact', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('typ_contact', self.gf('django.db.models.fields.CharField')(default='PRO', max_length=10)),
        ))
        db.send_create_signal('contact', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('contact_contact')


    models = {
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'cod_contact': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_contact': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tel_contact': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typ_contact': ('django.db.models.fields.CharField', [], {'default': "'PRO'", 'max_length': '10'})
        }
    }

    complete_apps = ['contact']