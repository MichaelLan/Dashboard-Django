from django import forms
from django.forms import TextInput, NumberInput
from .models import Proyecto

#TODO: hacer el formulario para cargar nuevos proyectos

class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['localidad', 'proyecto', 'tipo_proyecto', 'perfil_1', 'perfil_2', 
                'perfil_3', 'perfil_4', 'perfil_5', ]
        # exclude = ['created', 'updated', 'slug_localidad']
        widgets = {
            'localidad': TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Localidad'}),
            'proyecto': TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre del Proyecto'}),
            'tipo_proyecto': TextInput(attrs={'class':'form-control mt-3', 'placeholder': 'Tipo de proyecto'}),
            'perfil_1': NumberInput(attrs={'class':'form-control'}),
            'perfil_2': NumberInput(attrs={'class':'form-control'}),
            'perfil_3': NumberInput(attrs={'class':'form-control'}),
            'perfil_4': NumberInput(attrs={'class':'form-control'}),
            'perfil_5': NumberInput(attrs={'class':'form-control'}),
        }
        labels = {'localidad': '', 'proyecto':'', 'tipo_proyecto':'', 
                'perfil_1':'', 'perfil_2':'', 'perfil_3':'', 'perfil_4':'', 'perfil_5':''}
