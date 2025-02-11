# Classe 1
class Mamifero:
    def amamentar(self):
        return "Eu sou um mamífero e amamento meus filhotes."

# Classe 2
class Aquatico:
    def nadar(self):
        return "Eu sou um animal aquático e sei nadar."

# Classe 3 - Herança múltipla
class Golfinho(Mamifero, Aquatico):
    def som(self):
        return "Eu sou um golfinho e faço sons característicos!"

# Criando um objeto da classe Golfinho
golfinho = Golfinho()

# Chamando métodos herdados de Mamifero e Aquatico
print(golfinho.amamentar())  # Herança de Mamifero
print(golfinho.nadar())      # Herança de Aquatico
print(golfinho.som())        # Método próprio da classe Golfinho
