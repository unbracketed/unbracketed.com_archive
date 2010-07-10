from docutils import core

def format_rst(text):
    """format Restructured Text as HTML"""
    parts = core.publish_parts(source=text, writer_name='html4css1')
    return parts['fragment']