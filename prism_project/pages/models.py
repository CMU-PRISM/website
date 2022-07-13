from re import T
from django.db import models
from django.utils import timezone
from django.core.validators import validate_unicode_slug
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from string import capwords

class Page(models.Model):
    title = models.CharField(max_length=64, unique=True, validators=[validate_unicode_slug],
                             help_text="Use underscores '_' in place of spaces.") # title of page
    content = MarkdownxField(help_text="Find basic syntax tips at https://www.markdownguide.org/basic-syntax/") # interpret Markdownx to page
    date_created = models.DateTimeField(auto_now_add=True) # only keep the date and time of the most recent page update
    date_modified = models.DateTimeField(auto_now=True) # only keep the date and time of the most recent page update
    description = models.TextField(default="A page on the PRISM website!", max_length=256) # short description of page for directory
    show_in_sidenav = models.BooleanField(default=False,
                                          help_text="If true, list this page in the homepage's sidenav panel. Ideal for very important and/or popular pages") # do we list this page in the sidenav?
    show_in_navbar = models.BooleanField(default=False,
                                          help_text="If true, list this page in the navbar. Ideal for the first pages someone visiting the site might go to  (About, Contact, etc...)") # do we list this page in the sidenav?
    
    def __str__(self): # give string representation of the page object to be title and description
        return "%s | Last modified: %s | %s" % (self.pretty_title(), self.date_modified, self.description)
    
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content and self.date_modified == other.date_modified and self.description == other.description and self.date_created == other.date_created
    
    def __hash__(self):
        return super().__hash__()

    def formatted_markdown(self):
        return markdownify(self.content)
    
    def pretty_title(self):
        return capwords(self.title.replace("_", " ").strip())

    # Overwrite save to shift all title text to lowercase
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Page, self).save(*args, **kwargs)
