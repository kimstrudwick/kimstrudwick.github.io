from django.db import models
from django.urls import reverse

from markdownx.models import MarkdownxField


class Project(models.Model):
    title = models.CharField(max_length=60)
    medium = models.CharField(max_length=60)
    date = models.DateField()
    description = MarkdownxField()

    def get_absolute_url(self):
        return reverse("project", args=[self.pk])

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    title = models.CharField(max_length=30)
    description = MarkdownxField(blank=True)
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.PROTECT
    )
    upload = models.ImageField(upload_to="project_images")

    def __str__(self):
        return f"{self.project.title}: {self.title}"
