from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class List(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return f'{self.title}'


class Item(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (done={self.done})'


class Especialidade(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome


class Prestador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,
                                      verbose_name="Especialidade")  # relacionamento 1-n
    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Permite que 'user' seja nulo

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE, verbose_name="Prestador")
    data = models.DateField()

    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "13:00 ás 14:00"),
        ("5", "14:00 ás 15:00"),
    )
    horario = models.CharField(max_length=10, choices=Horarios)

    def __str__(self):
        return f'{self.prestador} - {self.get_horario_display()}'

class Atendimento(models.Model):
    agendas = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name="Agenda")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")

    def __str__(self):
        return f"Atendimento para {self.cliente} na agenda {self.agendas}"