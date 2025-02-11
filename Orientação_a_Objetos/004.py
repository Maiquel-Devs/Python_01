class Animal:
    def __init__(self, nome):
        self.nome = nome  

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  
        self.raca = raca        


cachorro = Cachorro("Rex", "Labrador")

print(cachorro.nome)  
print(cachorro.raca) 

# No construtor __init__ de Cachorro, usamos super().__init__(nome) para chamar o construtor da classe base, inicializando o atributo nome na instância.

# Os Atributos que se repetem manda no super() e os que não se repetem deixa na propria Classe