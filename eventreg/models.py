from django.db import models


# Create your models here.
class EventData(models.Model):
    eventName = models.CharField(max_length=264)
    eventDescription = models.TextField()
    eventVenue = models.CharField(max_length=50)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventSpeaker = models.CharField(max_length=50)
    numAttendees = models.IntegerField()