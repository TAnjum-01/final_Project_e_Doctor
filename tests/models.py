from django.db import models

# Create your models here.
from doctor.models import doctor
from patient.models import patient
from prescription.models import prescription
from testType.models import testType


class tests(models.Model):
    test_id = models.IntegerField(primary_key=True)
    testType_id = models.ForeignKey(testType, on_delete=models.CASCADE)
    date = models.DateTimeField()
    d_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    p_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    pres_id = models.ForeignKey(prescription, on_delete=models.CASCADE)