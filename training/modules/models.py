import uuid
from django.db import models
from courses.models import Course
from django.contrib.auth.models import User


class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    content = models.TextField()
    users = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    quiz = models.TextField()
    marks = models.IntegerField()

    def __str__(self):
        return self.quiz



class Response(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.TextField()
    score = models.IntegerField()
    
    def __str__(self):
        return self.answer


