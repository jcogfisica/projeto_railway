"""
No Django, apps.py é um arquivo de configuração encontrado em cada aplicação Django. Seu objetivo principal é fornecer configuração e
metadados específicos da aplicação para o framework Django.
"""

from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
