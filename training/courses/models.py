import uuid
from django.db import models
from django.contrib.auth.models import User


def get_image_dir(instance,filename):
    return 'course_images/{0}{1}'.format(uuid.uuid4(), filename)

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_dir)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    enrollees = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title