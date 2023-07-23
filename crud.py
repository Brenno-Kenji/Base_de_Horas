#------Importando_SQlite------#

import sqlite3 

#------Conectando_com_banco_de_dados------#

con = sqlite3.connect('Dados/Base_de_Horas.db')

#------Inserindo_dados_(C)------#

def h_insert_info(i):
    with con:
        cur = con.cursor()
        query = '''INSERT INTO horas (
        data,
        horario_entrada,
        horario_saida,
        informacoes_extras)
        VALUES (
        ?, ?, ?, ?
        )'''

        cur.execute(query, i)

#------Visualizando_dados_(R)------#

def h_access_info():
    array = []

    with con:
        cur = con.cursor()
        query = '''SELECT * FROM horas'''
        cur.execute(query)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array

#------Atualizando_dados_(U)------#

def h_update_info(i):
    with con:
        cur = con.cursor()
        query = '''UPDATE horas SET
        data = ?,
        horario_entrada = ?,
        horario_saida = ?,
        informacoes_extras = ? 
        WHERE id = ?'''

        cur.execute(query, i)

#------Deletando_dados_(D)------#
        
def h_delete_info(i):
    with con:
        cur = con.cursor()
        query = '''DELETE FROM horas WHERE id = ?'''

        cur.execute(query, i)

#------Filtrando_dados_(data)------#

def h_select_date(i):
    array = []

    with con:
        cur = con.cursor()
        query = '''SELECT * FROM horas WHERE data BETWEEN ? AND ?'''
        cur.execute(query, i)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array


        