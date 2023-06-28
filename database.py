import sqlite3 

con = sqlite3.connect('Dados/Base_de_Horas.db')

with con: 
    cur = con.cursor()
    cur.execute('''CREATE TABLE horas_trabalho(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    horario_entrada TEXT,
    horario_saida TEXT,
    informacoes_extras TEXT
    )''')