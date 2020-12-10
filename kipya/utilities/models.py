from cms.models.pluginmodel import CMSPlugin
import uuid
from django.db import models

class Iframe(CMSPlugin):
    iframe_code = models.TextField()

class ME2iCFP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    industry = models.CharField(max_length=255)
    idea = models.TextField()

    def __str__(self):
        return self.first_name + self.last_name


