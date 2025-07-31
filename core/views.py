"""
Em uma aplicação Django, views.py é um arquivo crucial que contém a lógica para lidar com requisições web e gerar respostas.
É um componente central da arquitetura Model-View-Template (MVT) do Django.
Uma view django nada mais é que uma função python.

django.shortcuts.render é uma função de atalho amplamente utilizada no Django que simplifica o processo de renderização
de um template HTML e seu retorno como um objeto HttpResponse.
A função combina as ações de:
1) Carregamento de um template especificado.
2) Combinação do template com um dicionário de contexto fornecido (dados).
3) Criação de um objeto HttpResponse contendo o HTML renderizado.

Esquema:

render(request, template_name, context=None, content_type=None, status=None, using=None)

Em especial, temos:
request: É o objeto HttpRequest recebido pela view.
template_name: É o nome do arquivo de template a ser renderizado, por exemplo: 'my_app/my_template.html'.
"""

from .models import Produto

from django.shortcuts import render  # shortcuts (atalhos) é um módulo da biblioteca django
from django.shortcuts import get_object_or_404 # retorna um objeto ou o erro 404
# django.http.HttpResponse refere-se à classe HttpResponse dentro do módulo django.http do Django.
# Esta classe é fundamental para o ciclo de solicitação-resposta do Django, pois cada função de visualização em uma aplicação Django é responsável por instanciar e
# retornar um objeto HttpResponse.
# Objetos HttpResponse representam a resposta HTTP que um aplicativo Django envia de volta ao cliente (por exemplo, um navegador da web) em resposta a uma solicitação.
# Objetos HttpResponse podem ser inicializados com um código de status HTTP (por exemplo, 200 para sucesso, 404 para não encontrado, 500 para erro do servidor).
from django.http import HttpResponse
# HttpResponseNotFound é uma classe do módulo django.http do Django usada para retornar uma resposta HTTP 404 Não Encontrado.
# Essa resposta indica que o recurso solicitado não foi encontrado no servidor.
from django.http import HttpResponseNotFound
# HttpResponseServerError é uma classe dentro do módulo django.http no framework web Django. Ela representa uma resposta HTTP com código de status 500,
# que indica um "Erro Interno do Servidor".
from django.http import HttpResponseServerError
# O módulo django.template.loader no Django fornece funções para carregar modelos dentro de um projeto Django.
# Ele atua como uma interface para os mecanismos de modelo configurados e seus respectivos carregadores, que são responsáveis por localizar e recuperar arquivos de modelo.
# Em particular, django.template.loader.get_template() é uma função no Django usada para carregar e recuperar um objeto de modelo compilado.
# Ele recebe um template_name (string) como seu argumento principal, que é o nome do arquivo de modelo a ser carregado.
# Após a recuperação bem-sucedida, ele retorna um objeto Template, que é uma representação compilada do modelo e pode ser usado para renderização.
from django.template import loader

# Quando digitamos no navegador "www.xxxx " e pressionamos "Enter", estamos fazendo uma requisição: por isso, o argumento da função index é o parâmetro request.
# Portanto, a nossa view recebe essa requisição, vinda do navegador. Claro que a view não recebe essa requisição diretamente.
# Antes de chegar na view, essa requisição passa pelo urls.py.
# View 1
def index(request):
    '''
    print(f'Request: {request}')
    print(f'dir(Request): {dir(request)}') # Exibe atributos e métodos
    print(f'Metodo: {request.method}') # Exibe o atributo metodo de request
    print(f'Headers: {request.headers}') # Exibe o cabeçalho: dicionário
    print(f"'User-Agent': {request.headers['User-Agent']}") #xibe o valor para a chave "User-Agent"
    print(f"User: {request.user}") # Usuário não logado: AnonymousUser; Usuário logado: jcog
    print(f"Dir(User): {dir(request.user)}")  # Atributos e métodos para o usuário
    print(f"Last Name: {request.user.last_name}")  # Atributo last_name para o usuário
    print(f"E-mail: {request.user.email}")  # Atributo email para o usuário
    # De forma simples, retornamos uma renderização do request, com um template, uma página html.
    # Geralmente, a página index.html é a página principal, a que carrega primeiro.
    '''

    produtos = Produto.objects.all() # retorna todos os objetos da classe Produto.objects

    teste = None

    if request.user == 'AnonymousUser':
        teste = 'Usuário não está logado!'
    else:
        teste = f'Usuário logado! Login: {request.user}'

    context = {
        'curso' : 'Programação Web com Django Framework',
        'outro' : 'Django é massa!',
        'logado' : teste,
        'produtos' : produtos # o valor do dicionário context para a chave 'produtos' é a lista de produtos
    } # context é um dicionário contendo valores que são retornados na renderização do "endereço raiz"

    return render(request, 'index.html', context) # renderização do endereço http

# View 2
def contato(request):
    # De forma simples, retornamos uma renderização do request, com um template, uma página html.
    # Geralmente, a página index.html é a página principal, a que carrega primeiro.
    return render(request, 'contato.html') # renderização do endereço http

# View 3
def produto(request, pk):
    # De forma simples, retornamos uma renderização do request, com um template, uma página html.
    # Geralmente, a página index.html é a página principal, a que carrega primeiro.
    print(f'PK: {pk}')
    # prod = Produto.objects.get(id = pk) # metodo get da classe Produto.objects retorna o produto pelo id
    prod = get_object_or_404(Produto.objects, id = pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context) # renderização do endereço http

# Configurando as "páginas não encontradas":
def error404(request, exception = None):
    template = loader.get_template('404.html')
    return HttpResponseNotFound(content = template.render(), content_type = 'text/html', charset = 'utf8', status = 404)
    #return HttpResponse(content=template.render(), content_type='text/html', charset='utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponseServerError(content = template.render(), content_type = 'text/html', charset = 'utf8', status = 500)
    #return HttpResponse(content=template.render(), content_type='text/html', charset='utf8', status=500)

