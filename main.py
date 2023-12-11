from flask import Flask, render_template
import secrets
from flask_wtf.csrf import CSRFProtect
from config import db, SQLALCHEMY_DATABASE_URI, login_manager
from routes.login import login_bp
from routes.item import item_bp
from routes.contato import contato_bp


app = Flask(__name__)

# Proteção necessária pro CRUD e Login
app.secret_key = secrets.token_hex(16)
csrf = CSRFProtect(app)

# Configuração de inicialização do Banco de Dados e Login
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
login_manager.init_app(app)

# Rotas utilizadas
app.register_blueprint(login_bp)
app.register_blueprint(item_bp)
app.register_blueprint(contato_bp)

# ROTAS
# index não uso mais aqui, pois o index lista os imóveis (está em item.py)
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/corretores')
def corretores():
    return render_template('corretores.html')

# Usado na primeira execução, para criar o banco de dados
app.app_context().push()
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
