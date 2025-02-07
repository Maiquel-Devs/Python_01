# Faltam 16 aulas de orientação a objetos.

# Função e Coleção

def Registrar(nome, idade):
    paciente = {'Nome': nome, 'Idade': idade}
    return paciente    # Retorna os Valores do paciente e não a função (Registrar)

paciente = Registrar('Paulo', 55) # O Registrar() guardará dentro da variavel global "paciente"
print(paciente['Nome'])

# Na função retorna apenas um valor (usando o return na função).

# Na variável dentro de uma função pode retornar mais de um valor e tambem pode retornar um valor
# de forma diferenciada  (usando o return na variável que fica dentro da função).