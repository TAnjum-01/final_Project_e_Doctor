
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class patient(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    p_id = models.IntegerField(primary_key=True)
    #age = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    dob = models.DateField()
