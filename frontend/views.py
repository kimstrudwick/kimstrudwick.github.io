import subprocess
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from frontend.models import Snippet, Project


def _get_about_text():
    return Snippet.objects.get(pk="about").text


def projects(request):
    projects = Project.objects.all()
    homepage_text = Snippet.objects.get(pk="homepage").text
    return render(
        request,
        "projects.html",
        {
            "projects": projects,
            "homepage_text": homepage_text,
            "about_text": _get_about_text(),
        },
    )


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(
        request, "project.html", {"project": project, "about_text": _get_about_text()}
    )

