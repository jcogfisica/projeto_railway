#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks.

    A função os.environ.setdefault(chave, valor) no Python é usada para definir uma variável de ambiente,
    mas apenas se ela ainda não estiver definida. Ela age como um setdefault de um dicionário,
    mas para o ambiente do sistema. Se a variável de ambiente já existir, o valor não será alterado.

    """

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django1.settings')
    try:
        #A linha from django.core.management import execute_from_command_line é uma instrução de importação padrão no Django,
        #normalmente encontrada no início de um arquivo manage.py dentro de um projeto Django.
        #Seu objetivo é importar a função execute_from_command_line, que é o ponto de entrada principal para a execução de comandos de
        #gerenciamento do Django. Essa função recebe uma lista de argumentos (semelhante a sys.argv) e os despacha para o comando de
        #gerenciamento apropriado do Django.
        #Quando você executa comandos como python manage.py runserver, python manage.py makemigrations ou python manage.py createsuperuser,
        #é execute_from_command_line que processa esses comandos e executa a lógica Django correspondente.
        #Isso centraliza o gerenciamento de várias tarefas administrativas e de desenvolvimento dentro de um projeto Django.

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    #Para rodar nosso projeto Django devemos digitar:
    #python manage.py runserver
    #exatamente no diretório onde se encontra o arquivo python manage.py.
    #Ao digitar e teclar "Enter" estamos passando o parâmetro "runserver" para o arquivo manage.py.
    #Olhe para a linha de código abaixo. A função execute_from_command_line recebe como parâmetro
    #sys.argv o qual é justamente "runserver" quando rodamos nosso projeto conforme comando logo acima.
    #Portanto, "runserver" é passado como parâmetro para a função
    #execute_from_command_line quando a aplicação é rodada.
    #O Django vem com um servidor web integrado com ele, escrito em python, o qual rodará
    #localmente nossa aplicação.

    execute_from_command_line(sys.argv)


if __name__ == '__main__':

    #Em Python, if __name__ == "__main__": é uma instrução condicional comum usada para determinar
    #se um script está sendo executado diretamente ou importado como um módulo.
    #Quando um arquivo Python é executado como o programa principal, a variável especial __name__ é
    #definida como "__main__". Se o arquivo for importado como um módulo para outro script, __name__
    #será definido como o nome do módulo (o nome do arquivo sem a extensão .py).
    #O código dentro do bloco if só será executado quando o script for executado diretamente,
    #tornando-se uma boa prática para definir o ponto de entrada do seu programa ou incluir código
    #de teste que não deve ser executado quando o arquivo for importado para outro lugar.

    main()
