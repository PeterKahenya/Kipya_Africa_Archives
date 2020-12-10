from django.db import models
from django.contrib.auth.models import User
from delegates.models import Attendee
import uuid

class Speaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendee = models.OneToOneField(Attendee,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)   