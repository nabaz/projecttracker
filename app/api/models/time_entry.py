from django.db import models
from project import Project
from task import Task
from django.contrib.auth.models import User
from api import Api
import datetime

class TimeEntry(Api):

    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    start_time = models.DateTimeField(blank=True, default=datetime.datetime.now)
    end_time = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)


    #TODO: current_user should be default for user
