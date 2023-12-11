# Lar Ideal Imóveis

### Sistema para uma imobiliária 
Projetinho criado em Flask, utilizando Python 3.11 e SQLITE


## Instalação

Criar ambiente virtual:
```
py -m venv venv
```

Instalar dependências, na pasta raíz do projeto:
```
pip install -r requirements.txt
```


## Execução

```
python main.py
```
A execução em localhost é na porta 5000
```
http://127.0.0.1:5000
```
Para acessar o modo admin, com as páginas do administrador
```
http://127.0.0.1:5000/login
usuário: admin
  senha: admin
```

### Estrutura do projeto
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
|   └───templates
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
