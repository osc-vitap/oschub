from django.db import models


# Create your models here.
class MailList(models.Model):
    email = models.EmailField(unique=True, editable=True)
