import os

from dateutil import parser
from django.conf import settings
from django_extensions.management.jobs import BaseJob
import simplejson as json
from twitter import Twitter

from unbracketed.apps.content.constants import CONTENT_SOURCE_TWITTER
from unbracketed.apps.content.models import Status


class Job(BaseJob):
    help = "import tweets"

    def execute(self):
        tweets = json.loads(open(os.path.join(os.path.dirname(__file__),'my_tweets.json')).read())
        #Example: 
        #{'favorited': False,
        # 'truncated': False,
        # 'text': 'researching social music and music aggregration services',
        # 'created_at': 'Mon Feb 23 01:37:46 +0000 2009',
        # 'source': 'web', 'in_reply_to_status_id': None,
        # 'in_reply_to_screen_name': None,
        # 'in_reply_to_user_id': None,
        # 'id': 1239002863}
        tweets.reverse()
        for tweet in tweets:
            status = Status(source = CONTENT_SOURCE_TWITTER)
            status.message = tweet['text']
            status.source_id = tweet['id']
            status.date_created = parser.parse(tweet['created_at'])
            status.save()
            print "SAVE %s" % tweet['text']
            
