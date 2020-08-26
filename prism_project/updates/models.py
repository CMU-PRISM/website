from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from prism_project import settings

class Update(models.Model):
    title = models.CharField(max_length=64, unique=True) # title of page
    content = MarkdownxField(max_length=512) # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    
    def __str__(self): # give string representation of the page object to be title and description
        return "%s %s %s %s %s" % (self.title, self.content, self.date_modified)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def slug_as_text(self):
        return str(self.title).replace(' ', '-').lower()