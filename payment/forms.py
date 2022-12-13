from django import forms
from payment.models import payment


class payment_form(forms.ModelForm):
    class Meta:
        model = payment
        fields = [
            'payment_id',
            'bill_no',
            'date',
        ]
