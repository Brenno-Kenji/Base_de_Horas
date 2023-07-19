#------Importando_SQlite------#

import sqlite3 

#------Conectando_com_banco_de_dados------#

con = sqlite3.connect('Dados/Base_de_Horas.db')

#--------------------------------------------
# Inserindo dados (C)
#--------------------------------------------

def insert_info(i):
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
# Acessar dados (R)
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

#--------------------------------------------
# Atualizando dados (U)
#--------------------------------------------

def update_info(i):
    with con:
        cur = con.cursor()
        query = '''UPDATE horas_trabalho SET
        data = ?,
        horario_entrada = ?,
        horario_saida = ?,
        informacoes_extras = ? 
        WHERE id = ?'''

        cur.execute(query, i)

#--------------------------------------------
# Deletando dados (D)
#--------------------------------------------
        
def delete_info(i):
    with con:
        cur = con.cursor()
        query = '''DELETE FROM horas_trabalho WHERE id = ?'''

        cur.execute(query, i)

#--------------------------------------------
# Filtrando data
#--------------------------------------------

def select_date(i):
    array = []

    with con:
        cur = con.cursor()
        query = '''SELECT * FROM horas_trabalho WHERE data BETWEEN ? AND ?'''
        cur.execute(query, i)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array


        