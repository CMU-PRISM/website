from django.db import models
from django.utils import timezone
from django.core.validators import validate_unicode_slug
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from prism_project import settings
from string import capwords

class Update(models.Model):
    title = models.CharField(max_length=64, unique=True, validators=[validate_unicode_slug]) # title of page
    content = MarkdownxField(max_length=512, help_text="Find basic syntax tips at https://www.markdownguide.org/basic-syntax/") # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update

    def __str__(self): # give string representation of the update object to be title
        return "%s | Last modified: %s" % (self.pretty_title(), self.date_modified)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def pretty_title(self):
        return capwords(self.title.replace("-", " ").replace("_", " ").strip())

    # Overwrite save to shift all title text to lowercase
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Update, self).save(*args, **kwargs)
