from django import forms
from prescription.models import prescription


class prescription_form(forms.ModelForm):
    class Meta:
        model = prescription
        fields = [
            'pres_id',
            'symptoms',
            'medicine'
            'd_id',
            'p_id',
        ]
