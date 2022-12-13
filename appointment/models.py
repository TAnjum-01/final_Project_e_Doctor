from django.db import models

# Create your models here.
from doctor.models import doctor
from patient.models import patient


class appointment(models.Model):
    ap_id = models.IntegerField(primary_key=True)
    d_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    p_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    serial = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100)