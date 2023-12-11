from flask import Blueprint, request, session, redirect, flash, url_for, render_template
from flask_login import login_user, login_required, logout_user
from models import User, LoginForm
from config import login_manager


login_bp = Blueprint('login_bp', __name__)

users = {'admin': {'username': 'admin', 'password': 'admin'}}  # Substitua com um armazenamento de usuários real

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) and users[username]['password'] == password:
            session['username'] = username
            user = User(username)
            login_user(user)
            flash('Login bem-sucedido!', 'success')  # Adiciona uma mensagem de sucesso
            return redirect(url_for('item_bp.index'))  # Redireciona para a página listar_itens
        else:
            flash('Nome de usuário ou senha inválidos', 'error')  # Adiciona uma mensagem de erro
    return render_template('login.html', form=form)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('item_bp.index'))
