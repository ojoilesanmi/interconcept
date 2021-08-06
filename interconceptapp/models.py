from django.db import models
from datetime import datetime

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.fullname

class Management(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    title = models.TextField(blank=False)
    linkedn_link = models.URLField(max_length=250, default=True)

    def __str__(self):
        return self.name



