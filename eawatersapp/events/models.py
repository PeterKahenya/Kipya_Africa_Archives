from django.db import models
from django.contrib.auth.models import User
import uuid
from  delegates.models import Delegate
from  attendees.models import Attendee
from speakers.models import Speaker
from guests.models import Guest


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starts_at = models.DateTimeField(auto_now=True,editable=False)
    ends_at = models.DateTimeField(auto_now=True,editable=False)
    name = models.CharField(max_length=256,blank=True,null=True)
    delegates = models.ManyToManyField(Delegate,blank=True)
    speakers = models.ManyToManyField(Speaker,blank=True)
    guests = models.ManyToManyField(Guest,blank=True)
    meeting_id = models.CharField(max_length=300,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def add_delegate(self,delegate):
        self.delegates.add(delegate)
        self.save()
        return True

class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendee = models.ForeignKey(Attendee,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)


    