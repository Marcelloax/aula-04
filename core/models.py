from django.db import models

class Equipamento(models.Model):
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ocupado = models.BooleanField(default=False)
    opcoes_prioridade = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=opcoes_prioridade, default='Média')

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    nascimento = models.DateField()
    idade = models.IntegerField()

class Categoria(models.Model):
    # Texto curto (max 100 letras)
    nome = models.CharField(max_length=100)
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
 
class Chamado(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, null=True, blank=True)

    equipamento = models.ForeignKey(Equipamento,on_delete=models.CASCADE, null=True, blank=True)

    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE, null=True, blank=True)

    # Texto curto (max 100 letras)
    laboratorio = models.CharField(max_length=100)
    
    # Texto longo (sem limite de letras)
    descricao = models.TextField()
    
    # Escolhas pré-definidas
    OPCOES_PRIORIDADE = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE, default='Média')
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.laboratorio} - {self.prioridade}"
    

    
