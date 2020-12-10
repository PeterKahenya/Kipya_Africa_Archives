from django.db import models
from boreholes.models import Meter
import uuid


class Readings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    time = models.BigIntegerField()
    rate = models.FloatField()
    total = models.FloatField()

    # def __init__(self):
    #     pass