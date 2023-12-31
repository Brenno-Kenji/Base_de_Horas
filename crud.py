#------Importando_SQlite------#

import sqlite3 

#------Conectando_com_banco_de_dados------#

con_hours = sqlite3.connect('Dados/Base_de_Horas.db')
con_activies = sqlite3.connect('Dados/Base_de_Atividades.db')

#------Base_de_Horas------#

##------Inserindo_dados_(C)------##

def h_insert_info(i):
    with con_hours:
        cur = con_hours.cursor()
        query = '''INSERT INTO horas (
        data,
        horario_entrada,
        horario_saida,
        informacoes_extras)
        VALUES (
        ?, ?, ?, ?
        )'''

        cur.execute(query, i)

##------Visualizando_dados_(R)------##

def h_access_info():
    array = []

    with con_hours:
        cur = con_hours.cursor()
        query = '''SELECT * FROM horas'''
        cur.execute(query)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array

##------Atualizando_dados_(U)------##

def h_update_info(i):
    with con_hours:
        cur = con_hours.cursor()
        query = '''UPDATE horas SET
        data = ?,
        horario_entrada = ?,
        horario_saida = ?,
        informacoes_extras = ? 
        WHERE id = ?'''

        cur.execute(query, i)

##------Deletando_dados_(D)------##
        
def h_delete_info(i):
    with con_hours:
        cur = con_hours.cursor()
        query = '''DELETE FROM horas WHERE id = ?'''

        cur.execute(query, i)

##------Filtrando_dados_(data)------##

def h_select_date(i):
    array = []

    with con_hours:
        cur = con_hours.cursor()
        query = '''SELECT * FROM horas WHERE data BETWEEN ? AND ?'''
        cur.execute(query, i)
        information = cur.fetchall()

        for i in information:
            array.append(i)

        return array

#------Base_de_Atividades------#

##------Inserindo_dados_(C)------##

def a_insert_info(i):
    with con_activies:
        cur = con_activies.cursor()
        query = '''INSERT INTO atividades (
        data,
        atividade,
        descricao,
        progresso)
        VALUES (
        ?, ?, ?, ?
        )'''

        cur.execute(query, i)

def a_access_info():
    
    list_data = []

    with con_activies:
        cur = con_activies.cursor()
        query = '''SELECT * FROM atividades'''
        cur.execute(query)
        information = cur.fetchall()

        for i in information:
            list_data.append(i)

        return list_data

def a_update_info(i):
    with con_activies:
        cur = con_activies.cursor()
        query = '''UPDATE atividades SET
        data = ?,
        atividade = ?,
        descricao = ?,
        progresso = ? 
        WHERE id = ?'''

        cur.execute(query, i)

def a_delete_info(i):
    with con_activies:
        cur = con_activies.cursor()
        query = '''DELETE 
        FROM atividades 
        WHERE id = ?'''

        cur.execute(query, i)

def a_select_info(i):
    
    values = []

    with con_activies:
        cur = con_activies.cursor()
        query = '''SELECT * FROM atividades WHERE atividade == ? AND data == ?'''
        cur.execute(query, i)
        information = cur.fetchall()

        for i in information:
            values.append(i)

        return values