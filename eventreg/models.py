from django.db import models
from django.urls import reverse


class Event(models.Model):
    eventName = models.CharField(max_length=264, unique=True)
    eventDescription = models.TextField()
    eventVenue = models.CharField(max_length=50)
    eventDate = models.DateField(editable=True)
    eventStartTime = models.TimeField(editable=True, default="20:00")
    eventEndTime = models.TimeField(editable=True, default="20:00")
    eventRegEndDate = models.DateField(editable=True)
    eventRegEndTime = models.TimeField(editable=True, default="20:00")
    eventSpeaker = models.TextField(editable=True)
    eventURL = models.URLField(editable=True)

    def get_absolute_url(self):
        return reverse("eventreg:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.eventName)


class EventUserData(models.Model):
    eventName = models.ForeignKey(Event, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=264, unique=True)
    studentReg = models.CharField(max_length=10, unique=True)
    studentEmail = models.EmailField(unique=True)
    studentRegistered = models.BooleanField(default=False)
    studentCheckedIn = models.BooleanField(default=False)
