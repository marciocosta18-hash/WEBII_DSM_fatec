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

from flask import Blueprint, render_template

paginas_bp = Blueprint('paginas', __name__, template_folder='templates')

@paginas_bp.route('/')
def index():
    return render_template('paginas/index.html', title='Página Inicial')