"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from markdownx import urls as markdownx

from frontend import views

urlpatterns = [
    path("", views.projects, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:project_id>", views.project, name="project"),
    path("admin/", admin.site.urls),
    path("markdownx/", include(markdownx)),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT,}
        ),
    ]
