from django.utils import timezone
from api import Api
from django.db import models

class Customer(Api):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	web_url = models.CharField(max_length=100)
	note = models.TextField()
	active = models.BooleanField()
