from django import  forms
from editais.models import Edital
from upload_validator import FileTypeValidator

class CriarEditalForm(forms.ModelForm):
  
    
    class Meta:
        model =Edital
        fields ='__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
            # 'nome': forms.CharField(label='label', max_length=100),
        }

class EditarEditalForm(forms.ModelForm):

    class Meta:
        model =Edital
        fields ='__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
            # 'nome': forms.CharField(label='label', max_length=100),
        }
