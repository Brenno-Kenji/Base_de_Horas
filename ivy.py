import tkinter as tk
from tkcalendar import Calendar, DateEntry
import sqlite3
import pandas as pd

# Functions

def new_data_base_hours():

    conection = sqlite3.connect('Dados/Base_de_Horas.db')

    c = conection.cursor()

    c.execute('''CREATE TABLE nome_da_empresa(
        Dia text,
        Hora_Entrada text,
        Hora_Fim text
        )
    ''')

    conection.commit()

    conection.close()

def sign_hour():

    conection = sqlite3.connect('Dados/Base_de_Horas.db')

    c = conection.cursor()

    c.execute('INSERT INTO nome_da_empresa VALUES (:Dia, :Hora_Entrada, :Hora_Fim)',
            {
                'Dia' : entry_dia.get(),
                'Hora_Entrada' : entry_entrada.get(),
                'Hora_Fim' : entry_saida.get()
            }
            ) 
        
    conection.commit() 

    conection.close()    

    entry_dia.delete(0, 'end') 
    entry_entrada.delete(0, 'end') 
    entry_saida.delete(0, 'end') 

def export_hours():

    conection = sqlite3.connect('Dados/Base_de_Horas.db')

    c = conection.cursor()

    c.execute(f'SELECT * FROM nome_da_empresa')

    horas_registradas = c.fetchall() 
    horas_registradas = pd.DataFrame(horas_registradas, columns = ['Dia', 'Hora_Entrada', 'Hora_Fim'])

    horas_registradas.to_excel('Dados/Base_Horas.xlsx')

    conection.commit() 

    conection.close() 

def insert_date():

    date_calendar = label_calendario.get_date()
    entry_dia.insert('end', date_calendar)

# Criando Tela de Registro: 

#-----------------------------------------------------
# Chamando a função abaixo, criamo uma base de dados:
# new_data_base_hours()
#-----------------------------------------------------

windows = tk.Tk()
windows.title('Ferramenta de base de horas pessoal')

#Labels:

label_calendario = Calendar(windows, fg = 'gray75', bg = 'blue', font = ('Times', '9', 'bold'), locale = 'pt_br')
label_calendario.grid(row = 0, column = 0, padx = 20, pady = 20)

label_dia = tk.Label(windows, text = 'Dia:')
label_dia.grid(row = 1, column = 0, padx = 10, pady = 10)

label_entrada = tk.Label(windows, text = 'Hora de Entrada')
label_entrada.grid(row = 2, column = 0, padx = 10, pady = 10)

label_saida = tk.Label(windows, text = 'Hora de Saida')
label_saida.grid(row = 3, column = 0, padx = 10, pady = 10)

#Entry:

entry_dia = tk.Entry(windows, width = 30)
entry_dia.grid(row = 1, column = 1, padx = 10, pady = 10)

entry_entrada = tk.Entry(windows, width = 30)
entry_entrada.grid(row = 2, column = 1, padx = 10, pady = 10)

entry_saida = tk.Entry(windows, width = 30)
entry_saida.grid(row = 3, column = 1, padx = 10, pady = 10)
    
#Criando os botoes:

button_cadastro = tk.Button(windows, text = 'Cadastrar Horário', command = sign_hour)
button_cadastro.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2, ipadx = 50)

button_export = tk.Button(windows, text = 'Exportar Base de Horas para Excel', command = export_hours)
button_export.grid(row = 5, column = 1, padx = 10, pady = 10, columnspan = 2, ipadx = 50)

button_date = tk.Button(windows, text = 'Inserir Data', command = insert_date)
button_date.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2, ipadx = 50)

windows.mainloop()