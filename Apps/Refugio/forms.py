from contextlib import nullcontext
from django import forms

class Refugio_form (forms.Form):

    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField()