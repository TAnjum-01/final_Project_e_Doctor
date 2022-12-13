from django.db import models
from doctor.models import doctor
from patient.models import patient


class prescription(models.Model):
    pres_id = models.IntegerField(primary_key=True)
    symptoms = models.TextField()
    medicine = models.TextField()
    d_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    p_id = models.ForeignKey(patient, on_delete=models.CASCADE)
