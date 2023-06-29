from django import forms
from .models import Fields
from datetime import datetime

class FieldsForm(forms.Form):
    class Meta:
        model = Fields
        fields = '__all__'