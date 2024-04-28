from django import forms
from django.contrib.auth.models import User
from .models import Atendimento, Especialidade, Prestador, Cliente, Agenda
import datetime
from django.core.exceptions import ValidationError


class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador

        fields = ('nome', 'email', 'telefone',
                  'especialidade')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Prestador'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = ('nome', 'cpf', 'email', 'sexo', 'telefone'
                  )

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'F'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EspForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('prestador', 'data', 'horario')

        widgets = {
            'prestador': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Remember to always return the cleaned data.
        return data



class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ('agendas', 'cliente')

        widgets = {
            'agendas': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

