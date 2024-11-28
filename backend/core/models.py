from django.db import models

# Create your models here.

from django.db import models

from django.db import models

from django.db import models

class TipoResiduo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default='Descrição não fornecida')  # Defina um valor padrão aqui

    def __str__(self):
        return self.nome


class LocalReciclagem(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tipo_residuo = models.ForeignKey(TipoResiduo, on_delete=models.CASCADE)
    imagens = models.ManyToManyField('Imagem', blank=True)

    def __str__(self):
        return self.nome

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagens_reciclagem/')
    
    def __str__(self):
        return f"Imagem {self.id}"

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
