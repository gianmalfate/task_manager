from django import forms
from .models import Tarefa


class AdicionarTarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ("descricao", "categoria")
        
class EditarTarefaForm(forms.Form):
    OPCOES_CATEGORIA = (
        ("urgente", "Urgente"),
        ("importante", "Importante"),
        ("precisa ser feito", "Precisa ser feito"),
    )

    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=OPCOES_CATEGORIA)