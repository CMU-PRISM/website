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
    slug_txt = str(title).replace(' ', '-').lower() # change spaces in title to underscores and create end of url
    slug = slugify(slug_txt)
    content = MarkdownxField() # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user()), default=None) # page should show who edited it and display "deleted" if the user has since been deleted
    desc = models.TextField(default="default description") # short description of page for directory
    
    def __str__(self): # give string representation of the page object to be "title by author"
        return "%s \n \n %s" % (self.title, self.desc)
    
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def get_slug(self):
        return self.slug

