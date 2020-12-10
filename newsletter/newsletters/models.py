from django.db import models
import uuid


class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=True, null=False, blank=False)
    newsletter_name=models.CharField(max_length=255)
    is_sent=models.BooleanField(default=False)


    def __str__(self):
        return self.newsletter_name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    content=models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=True, null=True, blank=True)


    def __str__(self):
        return self.content
