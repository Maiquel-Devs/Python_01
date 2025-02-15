from django.shortcuts import render
from datetime import date

def calcular_idade(request):
    idade = None
    if request.method == 'POST':
        data_nascimento = request.POST.get('Idade')
        if data_nascimento:
            # Converter a data de nascimento de string para um objeto date
            data_nascimento = date.fromisoformat(data_nascimento)
            hoje = date.today()
            
            # Calcular a idade
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    
    return render(request, 'idade_calculo/formulario.html', {'idade': idade})
