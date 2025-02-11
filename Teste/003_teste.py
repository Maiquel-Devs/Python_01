class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.idade}')

class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, profissao):
        super().__init__(nome, idade, sexo)
        self.profissao = profissao

Joao = Aluno('João', 55, 'M', 'Engenheiro')

Joao.info()