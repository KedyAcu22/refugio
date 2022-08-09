from contextlib import nullcontext
from django import forms


sexos = [(' Macho',' Macho'),(' Hembra',' Hembra')]
lista_especies = [(' Perro',' Perro'),(' Gato',' Gato')]

class Mascota_form (forms.Form):
    nickname = forms.CharField()
    especie = forms.ChoiceField(choices=lista_especies,required=True,label='Seleccione la especie')
    raza = forms.CharField()
    sexo =  forms.ChoiceField(choices=sexos,required=True,label='Seleccione el sexo')
    edad_aprox= forms.IntegerField(label='Edad aproximada')
    ingreso = forms.DateField()
    observaciones = forms.CharField()