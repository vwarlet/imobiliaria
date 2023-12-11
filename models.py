from wtforms import (StringField, IntegerField, SelectField, FileField, MultipleFileField, 
                     HiddenField, PasswordField, TextAreaField, SelectMultipleField)
from wtforms.validators import DataRequired, Optional, Email, Regexp
from flask_wtf import FlaskForm
from flask_login import UserMixin
from config import db
from static.utils import TIPOS, BAIRROS

# Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    csrf = HiddenField('CSRF Token')

# Tabela de associação muitos-para-muitos (cada imovel tem varias imagens)
item_imagem_association = db.Table('item_imagem_association',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), nullable=True),
    db.Column('imagem_id', db.Integer, db.ForeignKey('imagem.id'), nullable=True)
)

# Imovel
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=True)
    valor = db.Column(db.Integer, nullable=True)
    descricao = db.Column(db.String(1000), nullable=True)
    finalidade = db.Column(db.String(50), nullable=True)
    tipo = db.Column(db.String(50), nullable=True)
    bairro = db.Column(db.String(50), nullable=True)
    capa = db.Column(db.LargeBinary, nullable=True)
    imagens = db.relationship('Imagem', secondary=item_imagem_association, back_populates='itens')

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dados = db.Column(db.LargeBinary)
    itens = db.relationship('Item', secondary=item_imagem_association, back_populates='imagens')

class ItemForm(FlaskForm):
    titulo = StringField('Titulo')
    valor = IntegerField('Valor', validators=[Optional()])
    descricao = TextAreaField('Descrição')
    finalidade = SelectField('Finalidade', choices=[('alugar', 'Alugar'), ('comprar', 'Comprar')])
    tipo = SelectField('Tipo', choices=TIPOS)
    bairro = SelectField('Bairro', choices=BAIRROS)
    capa = FileField('Imagem de Capa (JPEG ou PNG)')
    imagens = MultipleFileField('Imagens (JPEG ou PNG)')
    # imagens = FileField('Imagens (JPEG ou PNG)', multiple=True)

# Formulário para filtros
class SearchForm(FlaskForm):
    bairro = SelectMultipleField('Bairro', choices=BAIRROS)
    tipo = SelectMultipleField('Tipo', choices=TIPOS)
    finalidade = SelectField('Finalidade', choices=[('todos', 'Comprar/Alugar'), ('alugar', 'Para Alugar'), ('comprar', 'Para Comprar')])
    valor_de = IntegerField('De')
    valor_a = IntegerField('Até')
    codigo = IntegerField('Código do Imóvel')

# Contato
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    mensagem = db.Column(db.String(1000))

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired(), Regexp(r'^\(\d{2}\)\s\d{4,5}-\d{4}$', message='Formato inválido de telefone')])
    email = StringField('Email', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
