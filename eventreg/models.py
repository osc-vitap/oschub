from django.db import models


# Create your models here.
class EventData(models.Model):
    eventName = models.CharField(max_length=264, unique=True)
    eventDescription = models.TextField()
    eventVenue = models.CharField(max_length=50)
    eventDate = models.DateField(editable=True)
    eventStartTime = models.TimeField(editable=True)
    eventEndTime = models.TimeField(editable=True)
    eventRegEndDate = models.DateField(editable=True)
    eventRegEndTime = models.DateField(editable=True)
    eventSpeaker = models.TextField(editable=True)
    eventURL = models.URLField(editable=True)

    def __str__(self):
        return str(self.eventName)


class EventUserData(models.Model):
    eventName = models.ForeignKey(EventData, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=264, unique=True)
    studentReg = models.CharField(max_length=10, unique=True)
    studentEmail = models.EmailField(unique=True)
    studentRegistered = models.BooleanField(default=False)
    studentCheckedIn = models.BooleanField(default=False)
