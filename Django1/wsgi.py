"""
WSGI config for Django1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

WSGI (Web Server Gateway Interface) é uma especificação que define como servidores web se
comunicam com aplicações web Python. É uma interface padrão que permite que diferentes servidores
web e frameworks Python funcionem juntos sem a necessidade de código específico para cada combinação.
Em essência, o WSGI atua como uma ponte, permitindo que um servidor web receba requisições HTTP e as
encaminhe para a aplicação Python, que por sua vez processa a requisição e retorna uma resposta ao
servidor, que a envia ao cliente.
Padrão de aplicações Python para web.
"""

import os

# get_wsgi_application() é uma função do Django que retorna um objeto chamável compatível com WSGI,
# atuando essencialmente como ponto de entrada para sua aplicação Django quando implantada usando um servidor WSGI.
# Ela é usada no arquivo wsgi.py do seu projeto Django para interagir com o servidor web.

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django1.settings')

application = get_wsgi_application()
