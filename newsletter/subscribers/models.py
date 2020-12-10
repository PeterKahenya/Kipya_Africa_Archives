from django.db import models
import uuid

class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254,unique=True)
    is_subscribed=models.BooleanField(default=True)
    special_token=models.CharField(blank=True,null=True,max_length=500)



    def __str__(self):
        return self.fullname
