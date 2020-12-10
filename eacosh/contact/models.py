from django.db import models

class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.full_name