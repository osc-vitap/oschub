from django.db import models


# Create your models here.
class EventData(models.Model):
    eventName = models.CharField(max_length=264, unique=True)
    eventDescription = models.TextField()
    eventVenue = models.CharField(max_length=50)
    eventDate = models.DateField(editable=True)
    eventStartTime = models.TimeField(editable=True)
    eventEndTime = models.TimeField(editable=True)
    eventSpeaker = models.TextField(editable=True)
    eventURL = models.URLField(editable=True)
# class EventUserData(models.Model):
