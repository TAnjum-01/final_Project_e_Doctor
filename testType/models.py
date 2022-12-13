from django.db import models

# Create your models here.


class testType(models.Model):
    testType_id = models.IntegerField(primary_key=True)
    testName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
