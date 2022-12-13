from doctor.models import doctor
from django import forms


class doctors_form(forms.ModelForm):
    class Meta:
        model = doctor
        fields = [
            'user',
            'd_id',
            'address',
            'speciality',
            'phone_number',
            'address',
            'BMDC_reg_no',
        ]
