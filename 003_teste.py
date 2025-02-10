class Animal:
    def __init__(self, nome):
        self.nome = nome  # Atributo 'nome' definido na classe base

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Reaproveita a inicialização do atributo 'nome'
        self.raca = raca        # Atributo 'raca' exclusivo de Cachorro

# Instanciando um objeto da classe Cachorro:
cachorro = Cachorro("Rex", "Labrador")

print(cachorro.nome)  # Acessa o atributo 'nome', definido na classe Animal
print(cachorro.raca)  # Acessa o atributo 'raca', exclusivo da classe Cachorro





