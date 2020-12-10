from django.db import models
from django.contrib.auth.models import User
import uuid

class Fundi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.OneToOneField(User)