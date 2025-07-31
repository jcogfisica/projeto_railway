# Na linha de código abaixo, estamos importando as funções (views django) index e contato do módulo views de nossa aplicação
from .views import index, contato, produto

from django.urls import path

urlpatterns = [
    # O nome de cada rota ou url é dado pelo atributo name de cada objeto
    path('', index, name = 'index'), # Nossa aplicação raiz, isto é, a página principal: por isso, é chamada index.
    # A aplicação "contato" é executada dentro de um caminho ou subdiretório dentro do site.
    # Isso significa que essa aplicação será "renderizada" em uma página ou seção específica dentro do site que está além da página inicial.
    # Em outras palavras, você está direcionando a renderização da aplicação para um local mais detalhado dentro da estrutura do site, além do endereço principal.
    path('contato', contato, name = 'contato'),
    path('produto/<int:pk>', produto, name = 'produto')
]

# Não é recomendado incluir todas as rotas no arquivo de rotas do projeto django
# Para cada aplicação, criamos um arquivo app.urls o qual listará as rotas específicas para a aplicação
# Ao final, usando a função include do módulo django.urls, incluímos as rotas para cada aplicação específica uma a uma dentro do projeto
# Portanto, cada aplicação terá o seu arquivo de rotas.
# E lá no arquivo de rotas de cada aplicação, teremos a aplicação de suas configurações, através da importação das views.
