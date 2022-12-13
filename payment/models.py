from django.db import models

# Create your models here.
from bill.models import bill


class payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    bill_no = models.ForeignKey(bill, on_delete=models.CASCADE)
    date = models.DateTimeField()