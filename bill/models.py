from django.db import models

# Create your models here.
from appointment.models import appointment


class bill(models.Model):
    bill_no = models.IntegerField(primary_key=True)
    amount = models.IntegerField(blank=True, null=True)
    ap_id = models.ForeignKey(appointment, on_delete=models.CASCADE)