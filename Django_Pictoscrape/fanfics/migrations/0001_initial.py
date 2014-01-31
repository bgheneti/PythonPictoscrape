# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FanFic'
        db.create_table(u'fanfics_fanfic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 31, 0, 0))),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'fanfics', ['FanFic'])

        # Adding model 'Keyword'
        db.create_table(u'fanfics_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fanfics.FanFic'])),
            ('key_word', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'fanfics', ['Keyword'])


    def backwards(self, orm):
        # Deleting model 'FanFic'
        db.delete_table(u'fanfics_fanfic')

        # Deleting model 'Keyword'
        db.delete_table(u'fanfics_keyword')


    models = {
        u'fanfics.fanfic': {
            'Meta': {'object_name': 'FanFic'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 31, 0, 0)'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'fanfics.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'key_word': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fanfics.FanFic']"})
        }
    }

    complete_apps = ['fanfics']