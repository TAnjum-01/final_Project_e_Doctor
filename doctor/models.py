from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class doctor(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    d_id = models.IntegerField(primary_key=True)
    speciality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    BMDC_reg_no = models.CharField(max_length=100)
