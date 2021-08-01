from django.db import models
from datetime import datetime

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.fullname


