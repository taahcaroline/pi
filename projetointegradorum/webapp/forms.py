from django import forms
from django.forms import ModelForm
from webapp.models import MeuFormulario 

class MeuFormularioForm(ModelForm):
    
      
    class Meta:
       model = MeuFormulario
       fields = ['usina', 'datainsp','opcoes', 'opcoes2', 'opcoes3', 'opcoes4', 'opcoes5', 'opcoes6', 'opcoes7', 'opcoes8',
      'opcoes9', 'opcoes10', 'opcoes11', 'opcoes12', 'opcoes13', 'opcoes14', 'opcoes15', 'observacoes1']

