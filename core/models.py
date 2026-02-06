from django.db import models
 
class Chamado(models.Model):
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
    

    
class Categoria(models.Model):
    # Texto curto (max 100 letras)
    nome = models.CharField(max_length=100)
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
    
class Equipamento(models.Model):
    descricao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=50)
    ocupado = models.BooleanField()

    OPCOES_CONDICAO = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Defeituoso', 'Defeituoso'),
    ]
    condicao = models.CharField(max_length=50, choices=OPCOES_CONDICAO, default='Novo')
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.tipo}"