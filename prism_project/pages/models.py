from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=128) # title of page
    content = MarkdownxField() # imterpret Markdownx in pages
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    author = models.ForeignKey(User, on_delete="[USER_DELETED]") # page should show who edited it and display "[USER_DELETED]" if the user has since been deleted
    
    def __str__(self): # give string representation of the page object to be "title by author"
        return "%s by %s" % (self.title, self.author)
    
    def formatted_markdown(self):
        return markdownify(self.content)
