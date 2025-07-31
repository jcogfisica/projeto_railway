"""
ASGI config for Django1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

O arquivo asgi.py em projetos Django é usado para configurar o comportamento assíncrono da aplicação.
Ele serve como a interface para servidores web assíncronos, permitindo que o Django lide com solicitações
de forma mais eficiente, especialmente útil para aplicações que exigem alta concorrência e suporte a
eventos em tempo real.
"""

import os

# A função get_asgi_application no Django é responsável por criar e retornar um aplicativo ASGI (Asynchronous Server Gateway Interface)
# que pode ser usado para lidar com requisições assíncronas. Em termos mais simples, ela prepara o seu projeto Django para trabalhar com
# protocolos como WebSockets e outros tipos de comunicação em tempo real, além do tradicional HTTP.

# Essa função, fornecida pelo pacote channels do Django, cria um objeto ASGI que pode ser usado pelo servidor para rotear requisições
# para os seus views e consumidores assíncronos.

# Em resumo, get_asgi_application é a ponte entre seu projeto Django e o mundo assíncrono, permitindo que você construa aplicações
# mais interativas e em tempo real.

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django1.settings')

application = get_asgi_application()
