# Lar Ideal Imóveis

Pequeno sistema de uma imobiliária.

Com sessão de login para o admin fazer CRUD de imóveis e visualizar mensagens enviadas pelos clientes.

O cliente pode buscar um imóvel através de filtros, acessar suas informações e enviar mensagem através do 'fale conosco'.


### Recursos utilizados

- Python 3.11
- Flask
- SQLITE


## Instalação

Criar ambiente virtual:

``
py -m venv venv
``

Instalar dependências, na pasta raíz do projeto:

``
pip install -r requirements.txt
``


## Execução

Na pasta raíz do projeto, rodar o comando:

``
python main.py
``

A execução em localhost é na porta 5000.

``
http://127.0.0.1:5000
``

Para acessar o modo admin, com as páginas do administrador:
```
http://127.0.0.1:5000/login
usuário: admin
  senha: admin
```


## Estrutura do projeto

```
imobiliaria
└───instance
│   │   imoveis_database.db
└───routes
│   │   __init__.py
│   │   contato.py
│   │   item.py
│   │   login.py
└───static
|   └───carousel
|   |   |   script.js
|   |   |   style.css
|   └───images
|   │   |  ...
|   └───styles
|   |   |   style.css
|   |   script.js
|   |   utils.py
└───templates
|   │   adicionar.html
|   │   corretores.html
|   │   editar.html
|   │   faleconosco.html
|   │   index.html
|   │   itens.html
|   │   layout.html
|   │   login.html
|   │   mensagens.html
|   │   perfil.html
|   │   quemsomos.html
|   .gitignore
|   config.py
|   main.py
|   models.py
|   README.md
|   requirements.txt
```

### Observação

O arquivo .env na raíz do projeto deveria ser removido, ele contém informações sensíveis como senhas de acesso e banco de dados.
Está aqui como demonstração, mas deve ser configurado no host do site, e adicionado ao .gitignore
```
FLASK_APP=main.py
FLASK_ENV=development
SENHA_ADMIN='admin'
DATABASE_URL='sqlite:///imoveis_database.db'
```
