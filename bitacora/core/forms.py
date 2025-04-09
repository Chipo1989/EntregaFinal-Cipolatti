from django import forms
from .models import Tarea, Stock

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada', 'fecha_creacion']
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nombre', 'descripcion', 'cantidad']