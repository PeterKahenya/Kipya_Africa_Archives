from django.db import models
import uuid

class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return self.name


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method = models.CharField(max_length=256,blank=True,null=True)
    amount = models.DecimalField(max_digits=9,decimal_places=2)
    code = models.CharField(max_length=256,blank=True,null=True)
    account = models.CharField(max_length=256,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return str(self.account)
