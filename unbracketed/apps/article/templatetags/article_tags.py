from django import template
from django.core.urlresolvers import reverse
from django.template import resolve_variable
from apps.article.models import Entry,Category

register = template.Library()


class EntryCategoryNode( template.Node ):
    
    def __init__(self,entry_var,varname):
        self.entry_var = template.Variable(entry_var)
        self.varname = varname
        
    def render(self, context ):
        entry_inst = self.entry_var.resolve(context)
        try:
            context[self.varname] = entry_inst.categories.all()[0]
        except IndexError:
            context[self.varname] = ''
            
        return ''


@register.tag
def entry_category( parser, token ):
    """
    A template tag that adds the Category of an Entry to the context

    Usage::

       {% entry_category [entry] as [varname]  %}


    [entry] is the Entry object
    [varname] is the name of context variable to set

    Example::

       {% entry_category entry as entry_cat %}
    """ 
    try:
        tag_name, entry_inst, keyword, varname = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly four arguments" % token.contents.split()[0]
    
    return EntryCategoryNode( entry_inst, varname )


class EntryCountByMonthNode( template.Node ):
    
    def __init__(self, date ):
        self.date = date
        
    def render( self,context ):
        try:
            actual_date = resolve_variable(self.date, context)
            return str(Entry.objects.filter( pub_date__year=actual_date.year, pub_date__month=actual_date.month ).count())
        except template.VariableDoesNotExist:
            return ''


@register.tag
def entry_count_for_month( parser,token ):
    """
    A template tag that renders the count of Entry objects for 

    Usage::

       {% entry_count_for_month [year] [month]  %}


    [year] is the year to lookup
    [month] is the month in [year] to determine the Entry count for specified as an integer (1 for January, 12 for December)

    Example::

       {% entry_count_for_month 2008 jan %}
    """
    try:
        tag_name, date = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly two arguments" % token.contents.split()[0]
   
    return EntryCountByMonthNode( date )


@register.inclusion_tag('article/entry_excerpt_list.html')
def entry_excerpt_list( entry_list ):
    """
    An inclusion template tag that renders the Entry instances using the excerpt field. 
    Good for listing article abstracts. 

    Usage::

       {% entry_excerpt_list [entry_list]  %}

    [entry_list] is a list or query set containing entries to render

    Example::

       {% entry_excerpt_list latest %}
    """
    return { 'blog_entry_list' : entry_list }


class ArchiveNode( template.Node ):
    """
    A template Node that renders an unordered list of the 3 most recent months that contain entries
    """
            
    def render(self, context ):
        
        dates = list(Entry.live.dates( 'pub_date', 'month', order='DESC' ))
        _fmt = '<li><a href="%s">%s</a></li>'
        try:
            return "<ul>" + ''.join( [ ( _fmt % (    reverse('article_entry_archive_month',args=[date.year,date.strftime('%b')]), date.strftime('%B') ) ) for date in dates[:3] ] ) + "</ul>"
        except IndexError:
            if len( dates ) == 0:
                return ''
            return "<ul>" + ''.join( [ ( _fmt % (reverse('article_entry_archive_month',args=[date.year,date.strftime('%b')]),date.strftime('%B')) ) for date in dates[:3] ] ) + "</ul>"


@register.tag
def archive_links( parser, token ):
    '''
    creates the output for the archive links section
    '''
    return ArchiveNode()



