
from south.db import db
from django.db import models
from unbracketed.apps.projects.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Project.tease'
        db.add_column('projects_project', 'tease', orm['projects.project:tease'])
        
        # Adding field 'Project.description_raw'
        db.add_column('projects_project', 'description_raw', orm['projects.project:description_raw'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Project.tease'
        db.delete_column('projects_project', 'tease')
        
        # Deleting field 'Project.description_raw'
        db.delete_column('projects_project', 'description_raw')
        
    
    
    models = {
        'projects.project': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_raw': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'repository_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'tease': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }
    
    complete_apps = ['projects']
