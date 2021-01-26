from django.db import models
from django.urls import reverse


class Event(models.Model):
    eventName = models.CharField(max_length=264)
    eventDescription = models.TextField()
    eventVenue = models.CharField(max_length=50)
    eventDate = models.DateField(editable=True)
    eventTime = models.TimeField(editable=True)
    eventSpeaker = models.TextField(editable=True)

    def get_absolute_url(self):
        return reverse("eventreg:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.eventName
