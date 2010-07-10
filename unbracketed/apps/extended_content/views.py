from django.utils import simplejson
from django.http import HttpResponse
from unipath.fspath import FSPath as Path
import pickle

#def delicious_django_tags( request ):
#    
#    f = open(  Path(__file__).parent.child('articles').child('django_delicious_tags').child('django-project-delicious-tags.pickle'), 'rb' )
#    tags = pickle.load( f )
#    f.close()
#    
#    return HttpResponse( simplejson.dumps(tags), mimetype="application/javascript" )
