from markdown import markdown
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def apply_markdown( request ):
    """
    apply Markdown markup to the data field in the request
    """
    markup = markdown( request.POST['data'], extensions=['codehilite'] )
    return render_to_response( 'utils/markup/markdown/preview.html',
                              {'preview':markup},
                              context_instance=RequestContext(request))

