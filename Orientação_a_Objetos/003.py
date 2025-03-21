# SuperClasse -> Classe Mãe
class Animal:
    def __init__(self, nome): # Método Construtor
        self.nome = nome

    def emitir_som(self):
        print("Au Au....")

# SubClasse -> Classe Filha
class Cachorro(Animal): # Herda todos os Atribtos e Métodos da Classe Mâe
    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo!")

# Instanciando apenas um objeto da classe Cachorro:
cachorro = Cachorro("Rex")
cachorro.emitir_som()    # Saída: Au Au....
cachorro.abanar_rabo()   # Saída: Rex está abanando o rabo!


# Como tem um Método Construtor na Classe Mãe ao intanciar um objeto na classe filha tem que colocar o astributos do método construtor na classe filha (ao nomear-la)
