"""
Em uma aplicação Django, o arquivo admin.py está localizado no diretório de cada aplicação individual e desempenha um papel crucial
na integração dos modelos dessa aplicação com a interface de administração do Django.
Seu objetivo principal é registrar os modelos da sua aplicação no site de administração do Django, permitindo que usuários confiáveis
(normalmente administradores ou funcionários) visualizem, criem, atualizem e excluam facilmente instâncias desses modelos por meio de
uma interface web intuitiva.
"""

# O Django oferece uma interface administrativa do nosso projeto (digite http://127.0.0.1:8000/admin/login/?next=/admin/ e tecle enter)
# Por padrão a autenticação (usuário e senha) vem através da aplicação auth (ver INSTALLED_APPS no arquivo de settings
# Quando passamos pela autenticação é criada uma sessão que é gerenciada pela aplicação sessions
# Há também uma troca de mensagens entre as aplicações que é gerenciada pela aplicação messages
# Poderemos utilizar arquivos estáticos (javascript, css, imagens, etc) graças à aplicação staticfiles
# Por fim, poderemos apresentar diferentes tipos de conteúdo por conta da aplicação contenttypes
# Para criar o usuário que será o administrador do sistema digite o comando:
# python manage.py createsuperuser
# Toda aplicação quando criada, é criado junto um arquivo admin.py o qual serve para registrar na administração os nossos modelos

from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin): # Classe ProdutoAdmin herda atributos e métodos de admin.ModelAdmin
    list_display = ('nome', 'preco', 'estoque') # Lista os atributos que queremos exibir no painel de administração do modelo

class ClienteAdmin(admin.ModelAdmin): # Classe ClienteAdmin herda atributos e métodos de admin.ModelAdmin
    list_display = ('nome', 'sobrenome', 'email') # Lista os atributos que queremos exibir no painel de administração do modelo

# As linhas de comando abaixo efetivamente "publicam" os modelos de dados na administração

admin.site.register(Produto, ProdutoAdmin) # Exbimos todos os atributos de cada registro
admin.site.register(Cliente, ClienteAdmin)  # Exbimos todos os atributos de cada registro

# Ao acessar o link da interface administrativa o site falará para você: na aplicação core, você tem dois modelos para administrar: Produtos e Clientes
