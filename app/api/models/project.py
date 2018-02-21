from customer import Customer
from django.contrib.auth.models import User
from api import Api
from django.db import models

class Project(Api):

    users = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    active = models.BooleanField(default=True)
