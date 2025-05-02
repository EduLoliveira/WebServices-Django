from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.endereco}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='empresas')

    def __str__(self):
        return self.nome