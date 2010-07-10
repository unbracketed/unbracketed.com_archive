
from south.db import db
from django.db import models
from unbracketed.apps.content.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Article'
        db.create_table('content_article', (
            ('id', orm['content.article:id']),
            ('active', orm['content.article:active']),
            ('date_created', orm['content.article:date_created']),
            ('date_modified', orm['content.article:date_modified']),
            ('source', orm['content.article:source']),
            ('source_id', orm['content.article:source_id']),
            ('meta_value', orm['content.article:meta_value']),
            ('tags', orm['content.article:tags']),
            ('author', orm['content.article:author']),
            ('title', orm['content.article:title']),
            ('slug', orm['content.article:slug']),
            ('status', orm['content.article:status']),
            ('body', orm['content.article:body']),
            ('excerpt', orm['content.article:excerpt']),
            ('enable_comments', orm['content.article:enable_comments']),
            ('featured', orm['content.article:featured']),
        ))
        db.send_create_signal('content', ['Article'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Article'
        db.delete_table('content_article')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'content.article': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'draft'", 'max_length': '10'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'content.bookmark': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'db_index': 'True'})
        },
        'content.protip': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'explanation_raw': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {})
        },
        'content.status': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['content']
