import subprocess
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from frontend.models import Project


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project.html", {"project": project})


def staticify(request):
    result = b""
    mirror_cmd = [
        "wget",
        "--no-host-directories",
        "--directory-prefix=.",
        "--mirror",
        "--convert-links",
        "--html-extension",
        "http://localhost:8000",
    ]
    result += subprocess.check_output(mirror_cmd)
    result += b"--------"
    git_cmd = ["git", "commit", "-am", "Generated static site"]
    result += subprocess.check_output(git_cmd)
    result += b"--------"
    git_cmd = ["git", "push"]
    result += subprocess.check_output(git_cmd)
    return HttpResponse(result)

