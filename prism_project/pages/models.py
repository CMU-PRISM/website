from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete="[USER_DELETED]")

