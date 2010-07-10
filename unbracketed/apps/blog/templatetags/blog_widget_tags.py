from django import template
from apps.article.models import Entry

register = template.Library()

#TODO: use stdlib functools
def media_includer( func ):
    def inner():
        from django.conf import settings
        context = func()
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@register.inclusion_tag('blog/widgets/recent_articles_widget.html')
@media_includer
def recent_articles_widget():
    """
    A page widget that renders a list of recent article entries
    Implemented as an inclusion tag.

    Usage::

       {% recent_articles_widget %}

    Example::

       {% recent_articles_widget %}
    """
    return {}

@register.inclusion_tag('blog/widgets/article_categories_widget.html')
@media_includer
def article_categories_widget():
    """
    A page widget that renders a list of all article categories
    Implemented as an inclusion tag.

    Usage::

       {% article_categories_widget %}

    Example::

       {% article_categories_widget %}
    """
    return {}


@register.inclusion_tag('blog/widgets/article_tags_widget.html')
@media_includer
def article_tags_widget():
    """
    A page widget that renders a list of the 5 most popular entry tags
    Implemented as an inclusion tag.

    Usage::

       {% article_tags_widget %}

    Example::

       {% article_tags_widget %}
    """
    return {}

@register.inclusion_tag('blog/widgets/search_widget.html')
@media_includer
def search_widget():
    """
    A page widget that renders search boxes for the site:
    -a Google Custom Search Engine for Unbracketed
    -DjangoSearch
    
    Implemented as an inclusion tag.

    Usage::

       {% search_widget %}

    Example::

       {% search_widget %}
    """
    return {}


@register.inclusion_tag('blog/widgets/article_archive_widget.html')
@media_includer
def article_archive_widget():
    """
    A page widget that renders the 3 most recent months that have
    articles
    
    Implemented as an inclusion tag.

    Usage::

       {% article_archive_widget %}

    Example::

       {% article_archive_widget %}
    """
    return {}


@register.inclusion_tag('blog/widgets/recent_bookmarks_widget.html')
@media_includer
def recent_bookmarks_widget():
    """
    A page widget that renders the most recent bookmarks
    
    Implemented as an inclusion tag.

    Usage::

       {% recent_bookmarks_widget %}

    Example::

       {% recent_bookmarks_widget %}
    """
    return {}


@register.inclusion_tag('blog/widgets/categories_topics_combo_widget.html')
@media_includer
def categories_topics_combo_widget():
    """
    A page widget that renders the most recent bookmarks
    
    Implemented as an inclusion tag.

    Usage::

       {% categories_topics_combo_widget %}

    Example::

       {% categories_topics_combo_widget %}
    """
    return {}
