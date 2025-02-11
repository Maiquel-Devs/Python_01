# É um extra do 004.py

# Super Classe
class Pessoa:
    def __init__(self, nome, idade, cpf):  # Atributos base "que tem que ter em qualque classe herdada"
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf

    def usuario(self):
        return f"Nome: {self.nome}, Idade: {self.idade} , CPF: {self.cpf}"
    
# Sub Classe
class Professor(Pessoa): 
    def __init__(self, nome, idade, cpf, materia):  # materia (atributo novo / diferente )
        super().__init__(nome, idade, cpf)
        self.materia = materia

    def prof_materia(self):
        print(f'Sou Professor de {self.materia}, e meu nome é {self.nome}.')

#Sub Classe
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, serie):   # serie (atributo novo / diferente)
        super().__init__(nome, idade, cpf)
        self.serie = serie

    def aluno_serie(self):
        print(f'Sou do(a) {self.serie} ano(a), e meu nome é {self.nome}.')


Luiz = Professor('Luiz', 56, '000-000-000-00', 'Matemática')

print(Luiz.nome)
Luiz.prof_materia()


Caio = Aluno('Caio', 15, '111-111-111-11', '8 ano')

print(Caio.nome)
Caio.aluno_serie()

print('--------------------------------------') # Essa linha é so para separar

print(Luiz.usuario()) # Estou dando print em um função por que no final dela tem um return 
print(Caio.usuario())

print('--------------------------------------')