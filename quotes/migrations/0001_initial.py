# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('quotes_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_bio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('quotes', ['Author'])

        # Adding model 'Tag'
        db.create_table('quotes_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('quotes', ['Tag'])

        # Adding model 'Quote'
        db.create_table('quotes_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('quotes', ['Quote'])

        # Adding M2M table for field authors on 'Quote'
        db.create_table('quotes_quote_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm['quotes.quote'], null=False)),
            ('author', models.ForeignKey(orm['quotes.author'], null=False))
        ))
        db.create_unique('quotes_quote_authors', ['quote_id', 'author_id'])

        # Adding M2M table for field tags on 'Quote'
        db.create_table('quotes_quote_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm['quotes.quote'], null=False)),
            ('tag', models.ForeignKey(orm['quotes.tag'], null=False))
        ))
        db.create_unique('quotes_quote_tags', ['quote_id', 'tag_id'])


    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('quotes_author')

        # Deleting model 'Tag'
        db.delete_table('quotes_tag')

        # Deleting model 'Quote'
        db.delete_table('quotes_quote')

        # Removing M2M table for field authors on 'Quote'
        db.delete_table('quotes_quote_authors')

        # Removing M2M table for field tags on 'Quote'
        db.delete_table('quotes_quote_tags')


    models = {
        'quotes.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_bio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'})
        },
        'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['quotes.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['quotes.Tag']", 'null': 'True', 'blank': 'True'})
        },
        'quotes.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['quotes']
