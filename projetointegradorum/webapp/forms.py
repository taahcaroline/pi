from django import forms
from django.forms import ModelForm
from webapp.models import MeuFormulario 

class MeuFormularioForm(ModelForm):
    
      
    class Meta:
       model = MeuFormulario
       fields = ['usina', 'datainsp','opcoes', 'opcoes2', 'opcoes3', 'opcoes4', 'opcoes5', 'opcoes6', 'opcoes7', 'opcoes8',
      'opcoes9', 'opcoes10', 'opcoes11', 'opcoes12', 'opcoes13', 'opcoes14', 'opcoes15', 'opcoes16', 'opcoes17', 'opcoes18', 'opcoes19', 'opcoes20', 'opcoes21', 'opcoes22', 'opcoes23', 'opcoes24',
      'opcoes25', 'opcoes26', 'opcoes27', 'opcoes28', 'opcoes29', 'opcoes30', 'opcoes31', 'opcoes32', 'observacoes1', 'observacoes2', 'observacoes3', 'observacoes4', 'observacoes5', 'observacoes6',
      'observacoes7', 'observacoes8', 'observacoes9', 'observacoes10', 'observacoes11', 'observacoes12', 'observacoes13', 'observacoes14', 'observacoes15', 'observacoes16',
      'observacoes17', 'observacoes18', 'observacoes19', 'observacoes20', 'observacoes21', 'observacoes22', 'observacoes23', 'observacoes24', 'observacoes25', 'observacoes26', 'observacoes27', 'observacoes28', 'observacoes29', 'observacoes30', 'observacoes31', 'observacoes32']

