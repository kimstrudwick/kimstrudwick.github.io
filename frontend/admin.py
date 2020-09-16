from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Project, ProjectImage, Snippet


admin.site.register(Project, MarkdownxModelAdmin)

admin.site.register(ProjectImage, MarkdownxModelAdmin)
admin.site.register(Snippet, MarkdownxModelAdmin)
