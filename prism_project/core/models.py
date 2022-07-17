from django.db import models
from django.utils import timezone

# Create your models here.

DOOR_STATES = (
    ('open', 'open'),
    ('closed', 'closed'),
    ('busy', 'busy'),
    ('unknown', 'unknown'),
)

class Door(models.Model):
    status = models.CharField(max_length=7, choices=DOOR_STATES, default="unknown")
    date_modified = models.DateTimeField(default=timezone.now) # only keep the date and time of the most recent update

    def __str__(self):
        time = self.date_modified.strftime("%x %H:%M")
        if self.status == 'open':
            return "OPEN as of %s" % time
        elif self.status == 'closed':
            return "CLOSED as of %s" % time
        elif self.status == 'busy':
            return "BUSY as of %s" % time
        else:
            return "DOOR STATUS UNKNOWN"

    def get_status(self):
        return self.status
