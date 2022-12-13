from django import forms
from tests.models import tests


class tests_form(forms.ModelForm):
    class Meta:
        model = tests
        fields = [
            'payment_id',
            'bill_no',
            'date',
        ]
