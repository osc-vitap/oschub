from django.db import models


class Speaker(models.Model):
    speakerName = models.CharField(max_length=64, editable=True)
    speakerProfession = models.CharField(max_length=64, editable=True)
    speakerImage = models.URLField(editable=True)

    def get_speakerImage (self):
        return "https://drive.google.com/uc?export=view&id={}".format(str(self.speakerImage.split('/')[5]))