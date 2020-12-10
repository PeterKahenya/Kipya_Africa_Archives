from django.db import models
from django.contrib.auth.models import User
import uuid


class Meter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.TextField()


class Borehole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    fetched_historical = models.BooleanField(default=False, null=True)

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    borehole = models.ForeignKey(Borehole,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=9,decimal_places=2)
    account_no = models.CharField(max_length=256)
    payment_method = models.CharField(max_length=256)

    def __str__(self):
        return self.payment_method