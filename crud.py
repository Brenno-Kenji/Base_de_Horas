#--------------------------------------------
# Importar SQlite
#--------------------------------------------

import sqlite3 

#--------------------------------------------
# Conectando com banco de dados
#--------------------------------------------

con = sqlite3.connect('Dados/Base_de_Horas.db')

#--------------------------------------------
# Inserindo informações (C)
#--------------------------------------------

def insert_inf(i):
    with con:
        cur = con.cursor()
        query = '''INSERT INTO horas_trabalho (
        data,
        horario_entrada,
        horario_saida,
        informacoes_extras)
        VALUES (
        ?, ?, ?, ?
        )'''

        cur.execute(query, i)

#--------------------------------------------
# Acessar informações (R)
#--------------------------------------------

def access_info():

    array = []

    with con:
        cur = con.cursor()
        query = '''SELECT * FROM horas_trabalho'''
        cur.execute(query)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array