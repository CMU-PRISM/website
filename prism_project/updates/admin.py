from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Update

# Register your models here.

admin.site.register(Update, MarkdownxModelAdmin)
