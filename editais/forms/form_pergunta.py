from django import forms
from django.forms import inlineformset_factory
from editais.models import Pergunta, Alternativa

class PerguntaForm(forms.ModelForm):
    is_aberta = forms.BooleanField(required=False, label='Esta pergunta é aberta')
    has_arquivo = forms.BooleanField(required=False, label='Esta pergunta requer arquivos')

    class Meta:
        model = Pergunta
        fields = ('descricao', 'is_aberta', 'has_arquivo')
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
            # 'nome': forms.CharField(label='label', max_length=100),
        }

        

class AltertativaForm(forms.ModelForm):

    class Meta:
        model= Alternativa
        fields='__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
            # 'nome': forms.CharField(label='label', max_length=100),
        }

Formset_PergAlter=inlineformset_factory(Pergunta,Alternativa,form=AltertativaForm, extra=1, can_delete=False )
        
        