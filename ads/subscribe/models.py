from django.db import models
import uuid

class ADSSubscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)

class KipyaPotentialLead(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname=models.CharField(max_length=200)
    organization=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    rfp_request=models.TextField()
