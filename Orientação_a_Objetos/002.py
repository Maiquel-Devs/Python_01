# Faltam 8 aulas de orientação a objetos.

"""  
def Registrar(nome, idade):
    paciente = {'Nome': nome, 'Idade': idade}
    return paciente    

paciente = Registrar('Paulo', 55) 
print(paciente['Nome'])

"""


class Cachorro:
    def __init__(self, nome): # Construtor 
        self.nome = nome  # Atributo

    def latir(self):  # Método 
        print(self.nome, "está latindo!")

    def correr(self):  # Método
        print(self.nome, "está correndo!")

# Criando instâncias da classe Cachorro
cachorro1 = Cachorro("Rex")   # --> Instancia (esse é seu objeto)
cachorro2 = Cachorro("Bob")


# Chamando atributos 
print(cachorro1.nome)
print(cachorro2.nome)

# Chamando os métodos
cachorro1.latir()
cachorro1.correr()

cachorro2.latir()
cachorro2.correr()


# 8:53 de aula 

