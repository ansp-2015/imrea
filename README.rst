=====
IMREA
=====


Configuração
------------

1. Report-builder
.................

1.1. Instalação

Seguir as instruções do site do `report-builder <https://django-report-builder.readthedocs.io/en/latest/quickstart/>`_.


1.2. Configuração

No arquivo settings.py do projeto, adicionar as linhas:
::
  REPORT_BUILDER_FRONTEND = True
  REPORT_BUILDER_INCLUDE = ['patient', ]

1.3. Verificar os ``statics``:

No projeto foram modificados os arquivos do report-builder do diretorio statics para melhorar o layout e implementar a tradução.
É possível verificar se o projeto está utilizando os arquivos corretos ao executar a aplicação. A página de configuração de relatórios deve estar em português.


2. django-reversion-compare
...........................

2.1. Instalação

Seguir as instruções do site do `django-reversion-compare <https://github.com/jedie/django-reversion-compare>`_.

Sempre que você registrar um modelo com django-reversion, execute ./manage.py createinitialrevisions


3. django-sql-explorer
......................
3.1. Instalação

Seguir as instruções do site do `django-sql-explorer <https://github.com/groveco/django-sql-explorer>`_.

