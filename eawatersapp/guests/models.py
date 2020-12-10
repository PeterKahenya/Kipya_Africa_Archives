from django.db import models
from django.contrib.auth.models import User
from delegates.models import Attendee

class Guest(models.Model):
    attendee = models.OneToOneField(Attendee,on_delete=models.CASCADE,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)   