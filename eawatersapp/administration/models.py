from django.db import models
import uuid
# Create your models here.
class AuthTokens(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.TextField()

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    your_name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    organization = models.TextField()
    issue = models.TextField()
    message = models.TextField()


    def __str__(self):
        return self.message





