from django import forms
from .models import Juegos, Promociones, Sorteos

class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = '__all__'

class PromocionesForm(forms.ModelForm):

    
    class Meta:
        model = Promociones
        fields = '__all__'

class SorteosForm(forms.ModelForm):        
    class Meta:
        model = Sorteos
        fields = '__all__'
        widgets = {
            "fecha": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }





