from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Profesor, Proyecto


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
