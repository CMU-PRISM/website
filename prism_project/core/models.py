from django.db import models
from django.utils import timezone

# Create your models here.

class Door(models.Model):
    is_open = models.BooleanField(null=True)
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent update

    def __str__(self):
        time = self.date_modified.strftime("%x %H:%M")
        if self.is_open == 1:
            return "OPEN as of %s" % time
        elif self.is_open == 0:
            return "CLOSED as of %s" % time
        else:
            return " DOOR STATUS UNKNOWN"