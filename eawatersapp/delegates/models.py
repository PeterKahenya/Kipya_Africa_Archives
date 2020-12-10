from django.db import models
from django.contrib.auth.models import User
from attendees.models import Attendee
import uuid
from payments.models import Payment


class Delegate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendee = models.OneToOneField(Attendee,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)


    def __str__(self):
        return self.attendee.user.first_name + "..."+self.attendee.user.last_name


class EAWATERS2020Delegate(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100,blank=True,null=True)
	first_name = models.CharField(max_length=100,blank=True,null=True)
	last_name = models.CharField(max_length=100,blank=True,null=True)
	email = models.EmailField(blank=True,null=True)
	country = models.CharField(max_length=100,blank=True,null=True)
	phone = models.CharField(max_length=15,blank=True,null=True)
	organization = models.CharField(max_length=255,blank=True,null=True)
	job_title = models.CharField(max_length=255,blank=True,null=True)
	association = models.CharField(max_length=255,blank=True,null=True)
	mpesa_code= models.CharField(max_length=255,blank=True,null=True)
	zoom_link= models.CharField(max_length=5000,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,editable=False)
	updated_at = models.DateTimeField(auto_now=True,editable=False)


	def __str__(self):
		return self.title + "..."+self.first_name + "..."+self.last_name
