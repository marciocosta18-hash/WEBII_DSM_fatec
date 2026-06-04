# -*- coding: utf-8 -*-
"""
Título: Blueprint de Páginas
Descrição: Arquivo contendo as rotas que renderizam templates HTML
Data: 28/04/2026
"""
__author__ = "Marcio Jose da Silva Costa"
__email__ = "marcio.costa01@aluno.cps.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"

from flask import Flask
from rotas import rotas_bp
from paginas import paginas_bp
from flask.json.provider import DefaultJSONProvider

class UTF8JSONProvider(DefaultJSONProvider):
    ensure_ascii = False

app = Flask(__name__)
app.json_provider_class = UTF8JSONProvider
app.json = UTF8JSONProvider(app)

# Registrando as blueprints
app.register_blueprint(rotas_bp)
app.register_blueprint(paginas_bp)

if __name__ == '__main__':
    app.run(debug=True)

    