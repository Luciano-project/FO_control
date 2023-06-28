from django import forms
from .models import Fields

class FieldsForm(forms.Form):
    factory_order = forms.CharField(max_length=10)
    factory_order_date = forms.DateField()
    article_number = forms.CharField(max_length=20)
    datasheet = forms.BooleanField()
    datasheet_date = forms.DateField()
    etools = forms.BooleanField()
    sticker = forms.BooleanField()
    sticker_date = forms.DateField()
    description = forms.CharField(max_length=200)
    client = forms.CharField(max_length=200)
