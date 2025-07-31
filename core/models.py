"""
Em um aplicativo Django, o arquivo models.py serve como local central para definir a estrutura de dados do
aplicativo e sua interação com o banco de dados. Este arquivo utiliza o Mapeador Objeto-Relacional (ORM) do
Django para representar tabelas de banco de dados como classes Python, permitindo operações de banco de
dados por meio de código Python em vez de SQL puro.
O padrão MVT (Model-View-Template) é a arquitetura utilizada pelo framework Django para organizar o desenvolvimento de
aplicações web. Ele divide a aplicação em três camadas principais: Modelo, Visão e Template, cada uma com suas responsabilidades específicas.
Através da definição de classes de objetos Python, o Django vai "criar" um banco ou estrutura de tabelas,
fazendo um mapeamento entre o arquivo de models e o banco de dados, utilizando o banco de dados como se fosse objetos Python.
"""

# O script 0001_initial.py cria um modelo de dados, isto é, cria um "schema" de dados
# Por padrão, o django usado um banco de dados que já vem integrado ao python 3, chamado sqlite3; veja o arquivo de settings do projeto django
# O banco de dados é criado toda vez que o projeto é executado
# Arquivos de migrations são criados toda vez que os modelos de dados forem alterados; isso permite ao django gerenciar e manter um histórico das alterações feitas
# Nota: o makemigrations só acessará as aplicações que estiverem constando do INSTALLED_APPS no arquivo settings.py
from django.db import models

# Definição de um modelo de dados: o objeto Produto tem os atributos definidos pela seguinte estrutura de dados:
class Produto(models.Model): # Produto é a classe filha e models.Model é a classe pai
    nome = models.CharField('Nome', max_length = 100)
    preco = models.DecimalField('Preço', max_digits = 10, decimal_places=2)
    estoque = models.IntegerField('Estoque')

    def __str__(self):  # Essa função serve para exibir os objetos de acordo com a definição de seu atributo nome
        return self.nome

class Cliente(models.Model): # Cliente é a classe filha e models.Model é a classe pai
    nome = models.CharField('Nome', max_length = 100)
    sobrenome = models.CharField('Sobrenome', max_length = 100)
    email = models.EmailField('E-mail', max_length = 100)

    def __str__(self):  # Essa função serve para exibir os objetos de acordo com a definição de seu atributo nome
        return self.nome


