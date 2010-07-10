from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
#from extended_content.views import delicious_django_tags

urlpatterns = patterns( '',
    #( r'^delicious-top-django-tag-cloud/testview/$', direct_to_template, {'template':'extended_content/delicious-top-django-tag-cloud.html'}  ),
    #( r'^delicious-top-django-tag-cloud/$', delicious_django_tags  ),
    ( r'^delicious-django-all-tag-cloud/$', direct_to_template, {'template':'extended_content/delicious-django-tag-cloud-all.html'}  ),
    ( r'^delicious-django-top25-tag-cloud/$', direct_to_template, {'template':'extended_content/delicious-django-tag-cloud-top25.html'}  ),
)