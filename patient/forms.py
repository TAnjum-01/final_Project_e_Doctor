from django import forms
from patient.models import patient


class patients_form(forms.ModelForm):
    class Meta:
        model = patient
        fields = [
            'user',
            'p_id',
            'phone_number',
            'address',
            'sex',
            'dob',
        ]
