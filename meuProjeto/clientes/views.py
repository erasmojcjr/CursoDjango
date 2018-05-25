from django.http import HttpResponse

def clientes(request):
    return HttpResponse('Maria,Jose,Joao')


def cliente_detalhe(request, id):
    if id == 1:
        return HttpResponse('Id Cliente 1')
    elif id == 2:
        return HttpResponse('Id Cliente 2')
    else:
        return HttpResponse('Id não cadastrado')

def cliente_nome (request, nome):
    return HttpResponse('ola ' + nome)
