from appointment.models import appointment
from django import forms


class appointment_form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = [
            'ap_id',
            'd_id',
            'p_id',
            'date',
            'serial',
            'description',
        ]
