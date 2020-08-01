from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from prism_project import settings

def get_sentinel_user(): # sets the user 'deleted' as the author of a post, should the post's author be deleted
    return None#User.objects.get_or_create(username='deleted')[0]

class Page(models.Model):
    title = models.CharField(max_length=128, unique=True) # title of page
    content = MarkdownxField() # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user()), default=None) # page should show who edited it and display "deleted" if the user has since been deleted
    desc = models.TextField(default="default description") # short description of page for directory
    
    def __str__(self): # give string representation of the page object to be title and description
        return "%s %s %s %s %s" % (self.title, self.content, self.date_modified, self.author, self.desc)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified and self.author == other.author and self.desc == other.desc
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def slug_as_text(self):
        return str(self.title).replace(' ', '-').lower()