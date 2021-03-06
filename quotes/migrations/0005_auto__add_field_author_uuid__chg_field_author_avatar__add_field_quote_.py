# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.uuid'
        db.add_column(u'quotes_author', 'uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Author.avatar'
        db.alter_column(u'quotes_author', 'avatar', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))
        # Adding field 'Quote.uuid'
        db.add_column(u'quotes_quote', 'uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.uuid'
        db.add_column(u'quotes_tag', 'uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Author.uuid'
        db.delete_column(u'quotes_author', 'uuid')


        # Changing field 'Author.avatar'
        db.alter_column(u'quotes_author', 'avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Deleting field 'Quote.uuid'
        db.delete_column(u'quotes_quote', 'uuid')

        # Deleting field 'Tag.uuid'
        db.delete_column(u'quotes_tag', 'uuid')


    models = {
        u'quotes.author': {
            'Meta': {'object_name': 'Author'},
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quotes.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quotes.Tag']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'quotes.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quotes']