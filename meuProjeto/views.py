from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    lista = [
        {'nome': 'Erasmo', 'sexo': 'm'},
        {'nome': 'Heitor', 'sexo': 'm'},
        {'nome': 'Pollyanna', 'sexo': 'f'}

    ]

    variaveis = {'lista': lista}
    return render(request, 'index.html', variaveis)



