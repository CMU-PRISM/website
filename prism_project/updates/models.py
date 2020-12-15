from django.db import models
from django.utils import timezone
from django.core.validators import validate_unicode_slug
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from prism_project import settings

class Update(models.Model):
    title = models.CharField(max_length=64, unique=True, validators=[validate_unicode_slug]) # title of page
    content = MarkdownxField(max_length=512) # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update

    def __str__(self): # give string representation of the page object to be title and description
        return "%s | Last modified: %s | %s" % (self.pretty_title(), self.date_modified, self.desc)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified and self.desc == other.desc
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def pretty_title(self):
        return self.title.replace("-", " ").replace("_", " ").capitalize().strip()