from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Page

# Register your models here.

admin.site.register(Page, MarkdownxModelAdmin)
