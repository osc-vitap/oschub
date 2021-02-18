from django.db import models


class Speaker(models.Model):
    speakerName = models.CharField(max_length=64, editable=True)
    speakerProfession = models.CharField(max_length=64, editable=True)
    speakerImage = models.URLField(editable=True)
