from dateutil import parser
from urllib import urlopen

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django_extensions.management.jobs import BaseJob
from pydelicious import DeliciousAPI

from unbracketed.apps.content.constants import CONTENT_SOURCE_DELICIOUS
from unbracketed.apps.content.models import Bookmark

class Job(BaseJob):
    help = "Updates Stream with recent Delicious posts"

    def execute(self):
        dapi = DeliciousAPI(settings.DELICIOUS_USER,settings.DELICIOUS_PASSWORD)
        for post in dapi.posts_recent()['posts']:
            try:
                bm = Bookmark.objects.get(source=CONTENT_SOURCE_DELICIOUS,
                                          source_id=post['hash'])
            except ObjectDoesNotExist:
                bookmark = Bookmark(source=CONTENT_SOURCE_DELICIOUS)
                bookmark.title = post['description']
                bookmark.url = post['href']
                bookmark.tags = post['tag']
                bookmark.description = post['extended']
                bookmark.source_id = post['hash']
                #bookmark.meta_value = post['meta']
                bookmark.date_created = parser.parse(post['time'])
                
                bookmark.save()
            else:
                break
        
