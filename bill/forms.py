from django import forms

from bill.models import bill


class bill_form(forms.ModelForm):
    class Meta:
        model = bill
        fields = [
            'bill_no',
            'amount',
            'ap_id',
        ]
