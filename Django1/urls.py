"""
URL configuration for Django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Em um projeto Django, urls.py é um arquivo que define os padrões de URL para sua aplicação.
Ele mapeia URLs para as funções de visualização (views) que lidam com as solicitações HTTP.
É essencial para o roteamento de URLs no Django.
O arquivo urls.py importa o módulo path (ou re_path para expressões regulares)
do django.urls e outras funções ou classes de visualização necessárias.
"""

from django.contrib import admin
from django.urls import path, include
# Em termos simples, um handler404 no contexto do Django é uma função ou view que é chamada quando um usuário tenta acessar uma página que não existe no seu site (um erro 404).
# Ele atua como um "tratador" de erros 404, permitindo que você personalize a experiência do usuário quando isso acontece.
# Em termos de desenvolvimento web, especialmente dentro do contexto do framework Django, handler500 refere-se a uma função de tratamento de erros que lida com erros
# internos do servidor, também conhecidos como erros HTTP 500. Esses erros ocorrem quando há problemas no código da sua view ou em outras partes do seu aplicativo
# durante o processamento da requisição.
from django.conf.urls import handler404, handler500
from core import views

# Na linha de código abaixo, estamos importando as funções (views django) index e contato do módulo views de nossa aplicação
from core.views import index, contato

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('core.urls')) # "Toda requisição que for para a raiz é enviada para a aplicação core: é ela quem vai receber essas requisições!"
]

# Não é recomendado incluir todas as rotas no arquivo de rotas do projeto django
# Para cada aplicação, criamos um arquivo app.urls o qual listará as rotas específicas para a aplicação
# Ao final, usando a função include do módulo django.urls, incluímos as rotas para cada aplicação específica uma a uma dentro do projeto
# Portanto, cada aplicação terá o seu arquivo de rotas.
# E lá no arquivo de rotas de cada aplicação, teremos a aplicação de suas configurações, através da importação das views.

handler404 = views.error404 # A visualização page_not_found() é substituída por handler404:
handler500 = views.error500 # A visualização server_error() é substituída por handler500:
