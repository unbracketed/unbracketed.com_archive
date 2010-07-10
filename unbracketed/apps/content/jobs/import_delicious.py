import os
from xml.etree.ElementTree import ElementTree as ET

from dateutil import parser
from django.conf import settings
from django_extensions.management.jobs import BaseJob
import simplejson as json

from unbracketed.apps.content.constants import (CONTENT_SOURCE_TWITTER,
                                                CONTENT_SOURCE_DELICIOUS)
from unbracketed.apps.content.models import Bookmark


class Job(BaseJob):
    help = "import delicious posts"

    def execute(self):
        et = ET()
        tree = et.parse(open(os.path.join(os.path.dirname(__file__),'my_delicious_posts.xml')))
        
        for post in tree.getchildren():
        
            #[('extended', ''),
            #('hash', 'c20a7fe7b722193ccb399104d818ebfd'),
            #('description', 'http://jtauber.com/2006/05/templates.html'),
            #('tag', 'python templates template html tutorial'),
            #('href', 'http://jtauber.com/2006/05/templates.html'),
            #('meta', '1b0af42a5c08535a22afa974d238e542'),
            #('time', '2009-08-31T17:37:30Z')]
            
            bookmark = Bookmark(source=CONTENT_SOURCE_DELICIOUS)
            bookmark.title = post.attrib['description']
            bookmark.url = post.attrib['href']
            bookmark.tags = post.attrib['tag']
            bookmark.description = post.attrib['extended']
            bookmark.source_id = post.attrib['hash']
            bookmark.meta_value = post.attrib['meta']
            bookmark.date_created = parser.parse(post.attrib['time'])
            
            bookmark.save()
            print "SAVE %s" % bookmark.title
            
        #recent_updates = twitter.statuses.user_timeline()
        #print recent_updates
