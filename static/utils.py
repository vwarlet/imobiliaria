import os

USERS = {'admin': {'username': 'admin', 'password': os.getenv('SENHA_ADMIN')}}

TIPOS = [
    ('casa', 'Casa'), 
    ('apartamento', 'Apartamento'), 
    ('terreno', 'Terreno'),
    ('comercial', 'Comercial')
]

BAIRROS = [
    ('naodefinido', 'Não Definido'),
    ('bomsucesso', 'Bom Sucesso'),
    ('carvalhobastos', 'Carvalho Bastos'),
    ('centenario', 'Centenário'),
    ('centro', 'Centro'),
    ('conegoluizwalterhanquet', 'Cônego Luiz Walter Hanquet'),
    ('donatereza', 'Dona Tereza'),
    ('drrosinha', 'Dr. Rosinha'),
    ('floresta', 'Floresta'),
    ('gaucho', 'Gaúcho'),
    ('generalantonionetto', 'General Antonio Netto'),
    ('getuliovargas', 'Getúlio Vargas'),
    ('hipico', 'Hípico'),
    ('jardim', 'Jardim'),
    ('jardimdeforte', 'Jardim de Forte'),
    ('mariadegraca', 'Maria de Graça'),
    ('oliveira', 'Oliveira'),
    ('olaria', 'Olaria'),
    ('ouroverde', 'Ouro Verde'),
    ('parqueresidencialdearroduro', 'Parque Residencial de Arroio Duro'),
    ('santabarbara', 'Santa Bárbara'),
    ('santamarta', 'Santa Marta'),
    ('saocarlos', 'São Carlos'),
    ('saojoao', 'São João'),
    ('saojose', 'São José'),
    ('saoluiz', 'São Luiz'),
    ('saopedro', 'São Pedro'),
    ('siajuliana', 'Siá Juliana'),
    ('vilanova', 'Vila Nova'),
    ('viegas', 'Viégas')
]

def obter_tipo_label(tipo_value):
    for value, label in TIPOS:
        if value == tipo_value:
            return label
    return None

def obter_bairro_label(tipo_value):
    for value, label in BAIRROS:
        if value == tipo_value:
            return label
    return None
