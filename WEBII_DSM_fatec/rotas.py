# -*- coding: utf-8 -*-
"""
Título: Blueprint de Rotas
Descrição: Arquivo contendo todas as rotas da aplicação
Data: 28/04/2026
"""
__author__ = "Marcio Jose da Silva Costa"
__email__ = "marcio.costa01@aluno.cps.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"


from flask import Blueprint, jsonify, request

rotas_bp = Blueprint('rotas', __name__)


# ─── Exercício 1 ───────────────────────────────────────────
@rotas_bp.route('/message')
def message():
    return 'Cadastro Salvo com sucesso', 200

# ─── Exercício 2 ───────────────────────────────────────────
# ─── Exercício 2 ───────────────────────────────────────────
@rotas_bp.route('/message/<int:status>')
def message_status(status):
    mensagens = {
        200: 'OK: Sucesso geral.',
        201: 'Created: Sucesso na criação.',
        400: 'Bad Request: Erro do cliente (sintaxe).',
        401: 'Unauthorized: Falta autenticação.',
        404: 'Not Found: Recurso não encontrado.',
        500: 'Internal Server Error: Erro no servidor.'
    }

    if status in mensagens:
        return f'{status} {mensagens[status]}', status
    else:
        return 'Status desconhecido', 400
    
# ─── Exercício 3 ───────────────────────────────────────────
@rotas_bp.route('/auth/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == 'genivaldo' and senha == 'jerusa':
        return jsonify({'status': 200, 'mensagem': 'OK: Sucesso geral.'}), 200
    else:
        return jsonify({'status': 401, 'mensagem': 'Unauthorized: Falta autenticação.'}), 401

# ─── Exercício 4 ───────────────────────────────────────────
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Validar primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Validar segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True


@rotas_bp.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')

    if not nome or not cpf:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Erro do cliente (sintaxe).'}), 400

    if validar_cpf(cpf):
        return jsonify({'status': 200, 'mensagem': 'OK: Sucesso geral.'}), 200
    else:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Erro do cliente (sintaxe).'}), 400
    
# ─── Exercício 5 ───────────────────────────────────────────
@rotas_bp.route('/convert/celsius/<temp>')
def converter_celsius(temp):
    try:
        temp = float(temp.replace(',', '.'))
        fahrenheit = temp * 1.8 + 32
        return jsonify({
            'celsius': temp,
            'fahrenheit': round(fahrenheit, 2)
        }), 200
    except ValueError:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Temperatura inválida.'}), 400
    
# ─── Exercício 6 ───────────────────────────────────────────
@rotas_bp.route('/search')
def search():
    q = request.args.get('q')

    if not q:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Parâmetro de busca obrigatório.'}), 400

    return jsonify({'status': 200, 'mensagem': f'Você pesquisou por: {q}'}), 200, \
           {'Content-Type': 'application/json; charset=utf-8'}

# ─── Exercício 7 ───────────────────────────────────────────
@rotas_bp.route('/api/register', methods=['POST'])
def register():
    nome = request.form.get('nome')
    idade = request.form.get('idade')

    if not nome or not idade:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Dados incompletos.'}), 400

    try:
        idade = int(idade)
    except ValueError:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Idade inválida.'}), 400

    if idade < 18:
        return jsonify({'erro': 'Cadastro permitido apenas para maiores de idade'}), 403

    return jsonify({'status': 201, 'mensagem': f'Usuário {nome} cadastrado'}), 201

# ─── Exercício 8 ───────────────────────────────────────────
@rotas_bp.route('/products')
def products():
    lista_produtos = [
        {'id': 1, 'nome': 'Notebook', 'preco': 3500.00},
        {'id': 2, 'nome': 'Mouse', 'preco': 150.00},
        {'id': 3, 'nome': 'Teclado', 'preco': 250.00}
    ]

    if not lista_produtos:
        return '', 204

    return jsonify(lista_produtos), 200

# ─── Exercício 9 ───────────────────────────────────────────
@rotas_bp.route('/admin/dashboard')
def dashboard():
    api_key = request.headers.get('X-Api-Key')

    if api_key == 'secret123':
        return jsonify({'status': 200, 'mensagem': 'Acesso ao painel administrativo liberado'}), 200

    return jsonify({'status': 401, 'mensagem': 'Unauthorized: Falta autenticação.'}), 401

