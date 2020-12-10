from django.db import models
from django.contrib.auth.models import User

class Attendee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    organization = models.CharField(max_length=255,blank=True,null=True)
    job_title = models.CharField(max_length=255,blank=True,null=True)
    association = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.user.first_name

    def attend(self, event):
        event.add_attendee(self)
        return True