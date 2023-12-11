from flask import Blueprint, redirect, url_for, render_template, Response, request
from flask_login import login_required
from models import Item, ItemForm, Imagem, SearchForm
from config import db
from static.utils import obter_bairro_label, obter_tipo_label


item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/itens')
@login_required
def itens():
    form = ItemForm()
    itens = Item.query.all()
    return render_template('itens.html', itens=itens, form=form)

@item_bp.route('/adicionar_item', methods=['GET', 'POST'])
@login_required
def adicionar_item():
    form = ItemForm()
    if form.validate_on_submit():
        titulo = form.titulo.data
        valor = form.valor.data
        descricao = form.descricao.data
        finalidade = form.finalidade.data
        tipo = form.tipo.data
        bairro = form.bairro.data
        capa = form.capa.data.read() if form.capa.data else None
        imagens = []
        for imagem in form.imagens.data:
            dados_imagem = imagem.read() if imagem else None
            imagens.append(Imagem(dados=dados_imagem))
        novo_item = Item(
            titulo=titulo, valor=valor if valor else None, descricao=descricao, 
            finalidade=finalidade, tipo=tipo, bairro=bairro, capa=capa, imagens=imagens
        )
        db.session.add(novo_item)
        db.session.commit()
        return redirect(url_for('item_bp.itens')) 
    return render_template('adicionar.html', form=form)

@item_bp.route('/editar_item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def editar_item(item_id):
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.titulo = form.titulo.data
        item.valor = form.valor.data
        item.descricao = form.descricao.data
        item.finalidade = form.finalidade.data
        item.tipo = form.tipo.data
        item.bairro = form.bairro.data
        capa_data = form.capa.data.read() if form.capa.data else None
        if capa_data:
            capa_data_bytes = bytes(capa_data)
            if item.capa:
                item.capa = capa_data_bytes
            else:
                nova_capa = Imagem(dados=capa_data_bytes)
                item.capa = nova_capa.dados
        novas_imagens = []
        for imagem_data in form.imagens.data:
            if imagem_data:
                imagem_data_bytes = bytes(imagem_data.read())
                nova_imagem = Imagem(dados=imagem_data_bytes)
                novas_imagens.append(nova_imagem)
        if novas_imagens:
            item.imagens = novas_imagens # substitui todas as imagens
          # item.imagens.extend(novas_imagens) # se eu quiser adicionar novas imagens (mantendo as existentes)
        db.session.commit()
        return redirect(url_for('item_bp.itens'))
    return render_template('editar.html', form=form, item=item)

@item_bp.route('/excluir_item/<int:item_id>', methods=['POST'])
@login_required
def excluir_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('item_bp.itens'))

@item_bp.route('/capa_item/<int:item_id>')
def capa_item(item_id):
    item = Item.query.get_or_404(item_id)
    return Response(item.capa, content_type='image/jpeg')

@item_bp.route('/imagens_item/imovel<int:item_id>/<int:imagem_id>')
def imagens_item(item_id, imagem_id):
    item = Item.query.get_or_404(item_id)
    imagem = next((img for img in item.imagens if img.id == imagem_id), None)
    return Response(imagem.dados, content_type='image/jpeg')

@item_bp.route('/imovel/<int:item_id>', methods=['GET', 'POST'])
def perfil(item_id):
    item = Item.query.get_or_404(item_id)
    tipo_value = obter_tipo_label(item.tipo)
    bairro_value = obter_bairro_label(item.bairro)
    return render_template('perfil.html', item=item, tipo_value=tipo_value, bairro_value=bairro_value)

@item_bp.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    resultados = None
    
    page = request.args.get('page', 1, type=int)  # Página atual, padrão para 1
    pagination = None
    # Filtros ao clicar em Buscar..
    if request.method == 'POST':
        codigo = form.codigo.data
        bairro = form.bairro.data
        tipo = form.tipo.data
        finalidade = form.finalidade.data
        valor_de = form.valor_de.data
        valor_a = form.valor_a.data

        query = Item.query
        if codigo:
            query = query.filter_by(id=codigo)
        if bairro:
             query = query.filter(Item.bairro.in_(bairro))
        if tipo:
            query = query.filter(Item.tipo.in_(tipo))
        if finalidade and finalidade != 'todos':
            query = query.filter_by(finalidade=finalidade)
        if valor_de:
            query = query.filter(Item.valor >= valor_de)
        if valor_a:
            query = query.filter(Item.valor <= valor_a)
        if valor_de and valor_a:
            query = query.filter(Item.valor.between(valor_de, valor_a))

        resultados = query.all()
    else:
        resultados = Item.query.all()
        pagination = Item.query.paginate(page=page, per_page=20, error_out=False)
        resultados = pagination.items

    return render_template('index.html', form=form, resultados=resultados, pagination=pagination)

@item_bp.route('/limpar_filtros', methods=['GET'])
def limpar_filtros():
    form = SearchForm() # Cria um novo formulário vazio
    # Redireciona para a rota principal ('/') sem os parâmetros de filtro
    return redirect(url_for('item_bp.index', **form.data))
