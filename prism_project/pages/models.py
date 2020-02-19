from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

def get_sentinel_user(): # sets the user 'deleted' as the author of a post, should the post's author be deleted
    return None#User.objects.get_or_create(username='deleted')[0]

class Page(models.Model):
    title = models.CharField(max_length=128) # title of page
    slug = 'page:' + str(title).replace(' ', '_') # change spaces in title to underscores and create end of url
    content = MarkdownxField() # interpret Markdownx to page
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent page update
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user()), default=None) # page should show who edited it and display "deleted" if the user has since been deleted
    link = "{% url clean_title %}" # link to any page should juse be prism.andrew.cmu.edu/pages/TITLE
    desc = models.TextField(default="default description") # short description of page for directory
    
    def __str__(self): # give string representation of the page object to be "title by author"
        return "%s by %s" % (self.title, self.author)
    
    def formatted_markdown(self):
        return markdownify(self.content)
