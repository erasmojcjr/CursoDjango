from django.db import models
#https://docs.djangoproject.com/en/2.0/ref/models/fields/#charfield

# Create your models here.

class Limitecredito(models.Model):
    descricao = models.CharField(max_length=50)
    limite = models.FloatField()

    def __str__(self):
        return self.descricao + ' ' + str(self.limite)


class CPF(models.Model):
    numero = models.CharField(max_length=11, blank=False)
    data_exp = models.DateField(auto_now=False)

    def __str__(self):
        return self.numero

class Banco(models.Model):
    banco = models.CharField(max_length=30)
    agencia = models.CharField(max_length=10)


    def __str__(self):
        return self.banco + ' ' + self.agencia


class Cliente(models.Model):
    nome = models.CharField(max_length=70, blank=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    cidade = models.CharField(max_length=70, blank=False, null=False)
    uf = models.CharField(max_length=2, blank=False, null=False)
    nascimento = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE) # relacionamento entre tabela 1 para 1
    limitecredito = models.ForeignKey(Limitecredito, on_delete=models.CASCADE, null=True, blank=True)
    banco = models.ManyToManyField(Banco, blank=True, null=True) # muito para muitos
    foto = models.ImageField(upload_to='clientes_fotos', blank=True, null=True)

    #usado para retornar a lista em nome no lugar de objeto
    def __str__(self):
        return self.nome



class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #relacionamento entre tabelas

    def __str__(self):
        return self.descricao + ' - ' + self.numero




