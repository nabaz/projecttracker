from django.db import models
from project import Project
from django.contrib.auth.models import User
from api import Api

class Task(Api):

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
