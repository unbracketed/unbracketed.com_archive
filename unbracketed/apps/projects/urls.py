from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from unbracketed.apps.projects.models import Project

urlpatterns = patterns('unbracketed.apps.projects.views',
        url('^$', object_list, {'queryset':Project.objects.all()}, name='projects_index'),
        url('^(?P<slug>.*)/$', 'project_detail', name='projects_project_detail'),
        #url('^(?P<slug>.*)/$', object_detail, {'queryset':Project.objects.get(slug=slug),'slug':slug},name='projects_project_detail'),        
)