# renderiza paginas html
# importar o httpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
# enviar dados da requisição
# parametro nome
def hello(request, nome, idade):
    # interpreta e responde para http
    return HttpResponse(f'<h1>Hello World, {nome} de {idade} anos<h1>')