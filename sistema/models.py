from django.db import models

    
#Aqui fica o model do funcionario
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(default="valor_padrao")
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    cargo = models.CharField(default="valor_padrao")
  
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    


    #Aqui fica o Model do idioma    
class Idioma(models.Model):
    nome = models.CharField(max_length=20)
    unidade = models.CharField(max_length=20)
    professor = models.ForeignKey(Funcionario, on_delete = models.CASCADE, default = '1',verbose_name = 'Ministrada')
    turno = models.CharField(default="valor_padrao")

    def __str__(self):
        return f'{self.nome}'
    

# Aqui fica o model do aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(default="valor_padrao")
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    id_idioma = models.ForeignKey(Idioma, on_delete = models.CASCADE, default = '1',verbose_name = 'idioma')


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'