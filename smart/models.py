import uuid
from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=256)
    amount=models.DecimalField(max_digits=9,decimal_places=2)
    account_no = models.CharField(max_length=256)
    payment_method = models.CharField(max_length=256)

    def __str__(self):
        return self.payment_method