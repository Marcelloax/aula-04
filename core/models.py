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

class Equipamentos(models.Model):
    descricao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=50)
    ocupado = models.BooleanField(default=False)
    
    OPICOES_CONDICAO = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Defeituoso', 'Defeituoso'),
    ]

    condicao = models.CharField(max_length=100, choices=OPICOES_CONDICAO, default="Novo")
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    nascimento = models.DateField()
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.cpf}"
        

