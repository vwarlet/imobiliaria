from flask import Blueprint, redirect, url_for, render_template, Response, request
from flask_login import login_required
from email.mime.text import MIMEText
from models import Contato, ContatoForm
from config import db
import smtplib


contato_bp = Blueprint('contato_bp', __name__)

@contato_bp.route('/mensagens')
@login_required
def contatos():
    contatos = Contato.query.all()
    form = ContatoForm()
    return render_template('mensagens.html', contatos=contatos, form=form)

@contato_bp.route('/excluir_mensagem/<int:contato_id>', methods=['POST'])
@login_required
def excluir_mensagem(contato_id):
    contato = Contato.query.get(contato_id)
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('contato_bp.contatos'))

@contato_bp.route('/faleconosco', methods=['GET', 'POST'])
def fale_conosco():
    form = ContatoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        telefone = form.telefone.data
        email = form.email.data
        mensagem = form.mensagem.data
        nova_mensagem = Contato(nome=nome, telefone=telefone, email=email, mensagem=mensagem)
        db.session.add(nova_mensagem)
        db.session.commit()
        return redirect(url_for('item_bp.index')) 
    return render_template('faleconosco.html', form=form)

@contato_bp.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    if request.method == 'POST':
        nome = request.form['nome']
        email_cliente = request.form['email']
        mensagem = request.form['mensagem']

        subject = f'Mensagem de {nome} ({email_cliente})'
        body = f'Mensagem: {mensagem}\n\nE-mail do cliente: {email_cliente}'

        # Configurações do servidor SMTP da empresa (apenas recebimento)
        smtp_server = 'smtp.live.com'
        smtp_port = 587  # Porta típica para SMTP

        # Configurar o e-mail
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = email_cliente  # Endereço de e-mail da empresa
        msg['To'] = 'vwarlet@hotmail.com'  # Endereço de e-mail da empresa

        # Conectar e enviar e-mail
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.sendmail(email_cliente, ['vwarlet@hotmail.com'], msg.as_string())

            return redirect(url_for('fale_conosco'))
        except Exception as e:
            return f"Erro ao enviar e-mail: {str(e)}"