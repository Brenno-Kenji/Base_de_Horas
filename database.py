#------Importando_SQlite------#

import sqlite3 

#------Criando_banco_de_dados_horas------#

def db_hours():

    con = sqlite3.connect('Dados/Base_de_Horas.db')

    #------Criando_tabela------#

    with con: 
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS horas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE,
        horario_entrada TEXT,
        horario_saida TEXT,
        informacoes_extras TEXT
        )''')

#------Criando_banco_de_dados_atividades------#

def db_activies():

    con = sqlite3.connect('Dados/Base_de_Atividades.db')

    #------Criando_tabela------#

    with con: 
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS atividades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE,
        atividade TEXT,
        descricao TEXT,
        progresso INT
        )''')

db_hours()
db_activies()
