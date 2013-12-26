# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'List'
        db.create_table(u'simplelist_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spec_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'simplelist', ['List'])

        # Adding model 'Entry'
        db.create_table(u'simplelist_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplelist.List'])),
            ('heading_text', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('body_text', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('doc_sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'simplelist', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'List'
        db.delete_table(u'simplelist_list')

        # Deleting model 'Entry'
        db.delete_table(u'simplelist_entry')


    models = {
        u'simplelist.entry': {
            'Meta': {'object_name': 'Entry'},
            'body_text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'doc_sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'heading_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplelist.List']"})
        },
        u'simplelist.list': {
            'Meta': {'object_name': 'List'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['simplelist']