from django import template

register = template.Library()

@register.inclusion_tag('debug/query_log.html')
def query_log( queries ):
    return { 'sql_queries' : queries }