from django import forms
from testType.models import testType


class testType_form(forms.ModelForm):
    class Meta:
        model = testType
        fields = [
            'testType_id',
            'testName',
            'description',
        ]
