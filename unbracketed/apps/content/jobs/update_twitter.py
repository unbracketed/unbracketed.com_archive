from dateutil import parser

from django.conf import settings
from django_extensions.management.jobs import BaseJob
from twitter import Twitter

from unbracketed.apps.content.constants import CONTENT_SOURCE_TWITTER
from unbracketed.apps.content.models import Status


class Job(BaseJob):
    help = "Twitter updater"

    def execute(self):
        twitter = Twitter(settings.TWITTER_USER,settings.TWITTER_PASSWORD)
        recent_updates = twitter.statuses.user_timeline()
        for tweet in recent_updates:
            try:
                status = Status.objects.get(source = CONTENT_SOURCE_TWITTER,
                                            source_id = str(tweet['id']))
            except Status.DoesNotExist:
                status = Status(source = CONTENT_SOURCE_TWITTER)
                status.message = tweet['text']
                status.source_id = str(tweet['id'])
                status.date_created = parser.parse(tweet['created_at'])
                status.save()
            else:
                break