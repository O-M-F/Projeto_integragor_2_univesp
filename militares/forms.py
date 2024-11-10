# forms.py
from django import forms
from .models import MilitarIncluso, TB_Vencimentos, MemorialDeCalculo, MemorialDeCalculo, OutrosMemorial


class MilitarInclusoForm(forms.ModelForm):
    incluir_hora_aula = forms.BooleanField(label='Incluir hora aula?', required=False)
    incluir_data_saida = forms.BooleanField(label='Incluir Data de Saida?', required=False)

    class Meta:
        model = MilitarIncluso
        fields = ['RE', 'posto_graduacao', 'nome', 'adicionais', 'dependentes', 'sexta_parte', 'hora_aula', 'data_agregacao', 'data_saida', 'oficio_dp', 'mes_referencia', 'pag_a_contar_de']
        widgets = {
            'data_agregacao': forms.DateInput(attrs={'type': 'date'}),
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
            'pag_a_contar_de': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_data_agregacao(self):
        data_agregacao = self.cleaned_data['data_agregacao']
        if data_agregacao:
            if isinstance(data_agregacao, str):
                try:
                    data_agregacao = datetime.datetime.strptime(data_agregacao, '%Y-%m-%d').date()
                except ValueError:
                    raise forms.ValidationError('Formato de data inválido. Use o formato aaaa-mm-dd.')
            elif not isinstance(data_agregacao, datetime.date):
                raise forms.ValidationError('Tipo de dado inválido para data.')
        return data_agregacao

    def clean_data_saida(self):
        data_saida = self.cleaned_data['data_saida']
        if data_saida:
            if isinstance(data_saida, str):
                try:
                    data_saida = datetime.datetime.strptime(data_saida, '%Y-%m-%d').date()
                except ValueError:
                    raise forms.ValidationError('Formato de data inválido. Use o formato aaaa-mm-dd.')
            elif not isinstance(data_saida, datetime.date):
                raise forms.ValidationError('Tipo de dado inválido para data.')
        return data_saida


from django import forms
from .models import TB_Vencimentos

class TBVencimentosForm(forms.ModelForm):
    class Meta:
        model = TB_Vencimentos
        fields = ['Posto_Grad', 'Codigo', 'Salario_Padrao', 'Cod_Funcao']



class MemorialDeCalculoForm(forms.ModelForm):
    class Meta:
        model = MemorialDeCalculo
        fields = [
            'protocolo_memorial', 'oficio_dp', 'RE_do_MilitarIncluso',
            'posto_graduacao', 'nome_MilitarIncluso', 'data_agregacao',
            'mes_referencia', 'salario_padrao', 'retp', 'adicionais',
            'sexta_parte', 'hora_aula', 'retp_incorp_hora_aula',
            'ats_incorp_hora_aula', 'sexta_parte_incorp_hora_aula',
            'outros', 'total_bruto', 'meses_serem_pagos',
            'total_empenhado', 'auxilio_reclusao', 'soma_total_pg'
        ]
        widgets = {
            'data_agregacao': forms.DateInput(attrs={'type': 'date'}),
        }

class OutrosMemorialForm(forms.ModelForm):
    class Meta:
        model = OutrosMemorial
        fields = ['nome_campo', 'valor']
