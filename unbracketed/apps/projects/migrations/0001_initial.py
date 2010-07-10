
from south.db import db
from django.db import models
from unbracketed.apps.projects.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', orm['projects.Project:id']),
            ('name', orm['projects.Project:name']),
            ('slug', orm['projects.Project:slug']),
            ('repository_url', orm['projects.Project:repository_url']),
            ('description', orm['projects.Project:description']),
        ))
        db.send_create_signal('projects', ['Project'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('projects_project')
        
    
    
    models = {
        'projects.project': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'repository_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['projects']
