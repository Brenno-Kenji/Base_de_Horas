#--------------------------------------------
# Importar bibliotecas
#--------------------------------------------

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import crud

#--------------------------------------------
# Funções 
#--------------------------------------------

#--------------------------------------------
# 1 - Cria a visualização da tabela 
#--------------------------------------------

def show_table():

    #--------------------------------------------
    # 1 - Criando titulos da tabela:
    #--------------------------------------------

    coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

    #--------------------------------------------
    # 2 - Criando dados:
    #--------------------------------------------

    data = crud.access_info()

    #--------------------------------------------
    # 3 - Criando tabela:
    #--------------------------------------------

    table = ttk.Treeview(right, selectmode = "extended", columns = coluna_header, show = "headings")
    bar_v = ttk.Scrollbar(right, orient = "vertical", command = table.yview)
    bar_h = ttk.Scrollbar( right, orient = "horizontal", command = table.xview)

    #--------------------------------------------
    # 4 - Visualizando tabela:
    #--------------------------------------------

    table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
    table.grid(column = 0, row = 0, sticky = 'nsew')
    bar_v.grid(column = 1, row = 0, sticky = 'ns')
    bar_h.grid(column = 0, row = 1, sticky = 'ew')

    right.grid_rowconfigure(0, weight = 12)

    #--------------------------------------------
    # 5 - Configurando alinhamento e tamanho:
    #--------------------------------------------

    alignment = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    size = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in coluna_header:
        table.heading(col, text = col.title(), anchor = tk.CENTER)
        table.column(col, width = size[n], anchor = alignment[n])
        
        n += 1

    for item in data:
        table.insert('', 'end', values = item)

#-------------------------------------------------
# 2 - Insere os dados no banco de dados e tabela 
#-------------------------------------------------

def insert():
    date = e_date.get()
    entry_time = e_entry_time.get()
    exit_time = e_exit_time.get()
    observation = e_observation.get()

    array = [date, entry_time, exit_time, observation]

    if date == '' or entry_time == '' or exit_time == '':
        messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
    else:
       crud.insert_inf(array)
       messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

       e_date.delete(0, 'end')
       e_entry_time.delete(0, 'end')
       e_exit_time.delete(0, 'end')
       e_observation.delete(0, 'end')
    
    for widget in right.winfo_children():
        widget.destroy()

    show_table()

#--------------------------------------------
# Definindo cores
#--------------------------------------------

co0 = '#f0f3f5' # Preto
co1 = '#feffff' # Branco
co2 = '#4fa882' # Verde
co3 = '#38576b' # Valor
co4 = '#403d3d' # Letra
co5 = '#e06636' # - Profit
co6 = '#038cfc' # Azul
co7 = '#ef5350' # Vermelho
co8 = '#263238' # + Verde
co9 = '#e9edf5' # Sky blue

#--------------------------------------------
# Criando janela: 
#--------------------------------------------

windows = tk.Tk()
windows.title('Ferramente de base de horas - Criada por Brenno Kenji (versão: 0.2)')
windows.geometry('898x453')
windows.configure(background = co9)
windows.resizable(width = False, height = False)

#--------------------------------------------
# Dividindo janela: 
#--------------------------------------------

left_top = tk.Frame(windows, width = 310, height = 50, background = co2, relief = 'flat')
left_top.grid(row = 0, column = 0)

left_down = tk.Frame(windows, width = 310, height = 403, background = co1, relief = 'flat')
left_down.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 0, pady = 1)

right = tk.Frame(windows, width = 588, height = 403, background = co1, relief = 'flat')
right.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

#--------------------------------------------
# Criando labels e entrys: 
#--------------------------------------------

#--------------------------------------------
# 1 - Criando titulo: 
#--------------------------------------------

app_name = tk.Label(left_top, text = 'Base de Horas - Pessoal', anchor = tk.NW, font = ('Ivy 13 bold'), background = co2, fg = co1, relief = 'flat')
app_name.place(x = 10, y = 20)

#--------------------------------------------
# 1 - Criando campo "Data":
#--------------------------------------------

l_date = tk.Label(left_down, text = 'Data do expediente: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_date.place(x = 10, y = 40)
e_date = DateEntry(left_down, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2)
e_date.place(x = 160, y = 40)

#--------------------------------------------
# 2 - Criando campo "Horário de entrada":
#--------------------------------------------

l_entry_time = tk.Label(left_down, text = 'Horário de entrada: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_entry_time.place(x = 10, y = 100)
e_entry_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_entry_time.place(x = 160, y = 100)

#--------------------------------------------
# 3 - Criando campo "Horário de saida":
#--------------------------------------------

l_exit_time = tk.Label(left_down, text = 'Horário de saida: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_exit_time.place(x = 10, y = 160)
e_exit_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_exit_time.place(x = 160, y = 160)

#--------------------------------------------
# 4 - Criando campo "Observações":
#--------------------------------------------

l_observation = tk.Label(left_down, text = 'Observações: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_observation.place(x = 10, y = 220)
e_observation = tk.Entry(left_down, width = 35, justify = 'left', relief = 'solid')
e_observation.place(x = 15, y = 250)
    
#--------------------------------------------
# Criando botoes: 
#--------------------------------------------

#--------------------------------------------
# 1 - Criando botão "Inserir":
#--------------------------------------------

b_input = tk.Button(left_down, command = insert, text = 'Inserir', width = 7, font = ('Ivy 8 bold'), background = co6, fg = co1, relief = 'raised', overrelief = 'ridge')
b_input.place(x = 15, y = 310)

#--------------------------------------------
# 2 - Criando botão "Atualizar":
#--------------------------------------------

b_update = tk.Button(left_down, text = 'Atualizar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
b_update.place(x = 115, y = 310)

#--------------------------------------------
# 3 - Criando botão "Deletar":
#--------------------------------------------

b_delete = tk.Button(left_down, text = 'Deletar', width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
b_delete.place(x = 215, y = 310)

#--------------------------------------------
# Visualizando tabela: 
#--------------------------------------------

show_table()

#--------------------------------------------
# Mantendo o sistema em loop: 
#--------------------------------------------

windows.mainloop()