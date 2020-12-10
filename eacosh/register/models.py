import uuid
from django.db import models

class Attendee2020(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    organization=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    gak_no=models.CharField(max_length=100,blank=True,null=True)
    country=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    mpesa_code=models.CharField(max_length=100,blank=True,null=True)
    mpesa_name=models.CharField(max_length=100,blank=True,null=True)
    mpesa_amount=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.first_name+" "+self.last_name