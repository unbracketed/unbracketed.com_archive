from datetime import datetime
from unbracketed.apps.stream.models import Stream


def add_stream_item(sender,**kwargs):
    """post_save signal receiver that adds the sender to the content stream"""
    instance = kwargs['instance']
    created = kwargs['created']
    item = Stream(content_object=instance)
    if created:
        item.date_created = instance.date_created
    else:
        item.date_updated = datetime.now()
    item.save()