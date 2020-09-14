from django.shortcuts import get_object_or_404, render
from frontend.models import Project


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project.html", {"project": project})
