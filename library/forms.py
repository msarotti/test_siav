from django import forms
from .models import Book


class ImportJSONForm(forms.Form):
    json_file = forms.FileField()
