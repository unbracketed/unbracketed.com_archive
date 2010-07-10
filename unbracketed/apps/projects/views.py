from django.views.generic.list_detail import object_detail
from unbracketed.apps.projects.models import Project


def project_detail(request,slug):
    return object_detail(request,Project.objects.all(),slug=slug)


