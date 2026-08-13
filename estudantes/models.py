from django.db import models

# Classe de dados a ser utilizada para relacionamento entre objetos (quando instanciada)
# e também como vinculação com o banco de dados.
class Estudantes(model.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    nascimento = models. DateField()
    senha = models.CharField(max_length=16)
