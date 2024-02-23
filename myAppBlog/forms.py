from django import forms
from .models import Comentarios

class FormularioComentarios(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'email', 'contenido', 'activo', 'fkPost']