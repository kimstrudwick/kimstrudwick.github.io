from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Project, ProjectImage


admin.site.register(Project, MarkdownxModelAdmin)

admin.site.register(ProjectImage, MarkdownxModelAdmin)
