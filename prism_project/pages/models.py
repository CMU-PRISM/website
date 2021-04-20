from django.db import models
from django.utils import timezone
from django.core.validators import validate_unicode_slug
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from prism_project import settings
from string import capwords

class Page(models.Model):
    title = models.CharField(max_length=64, unique=True, validators=[validate_unicode_slug]) # title of page
    content = MarkdownxField() # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    desc = models.TextField(default="default description", max_length=256) # short description of page for directory
    
    def __str__(self): # give string representation of the page object to be title and description
        return "%s | Last modified: %s | %s" % (self.pretty_title(), self.date_modified, self.desc)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified and self.desc == other.desc
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def pretty_title(self):
        return capwords(self.title.replace("-", " ").replace("_", " ").strip())

    # Overwrite save to shift all title text to lowercase
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Page, self).save(*args, **kwargs)