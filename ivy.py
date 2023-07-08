#--------------------------------------------
# Importar bibliotecas
#--------------------------------------------

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import crud

#--------------------------------------------
# Variáveis globais 
#--------------------------------------------

global table #Retorna o valor de table como uma variável global

#--------------------------------------------
# Funções 
#--------------------------------------------

#--------------------------------------------
# 1 - Cria a visualização da tabela 
#--------------------------------------------

def show_table():

    global table # Faz a variável local se tornar local

    #--------------------------------------------
    # 1.1 - Criando titulos da tabela:
    #--------------------------------------------

    coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

    #--------------------------------------------
    # 1.2 - Criando dados:
    #--------------------------------------------

    data = crud.access_info()

    #--------------------------------------------
    # 1.3 - Criando tabela:
    #--------------------------------------------

    table = ttk.Treeview(right_down, selectmode = "extended", columns = coluna_header, show = "headings")
    bar_v = ttk.Scrollbar(right_down, orient = "vertical", command = table.yview)
    bar_h = ttk.Scrollbar(right_down, orient = "horizontal", command = table.xview)

    #--------------------------------------------
    # 1.4 - Visualizando tabela:
    #--------------------------------------------

    table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
    table.grid(column = 0, row = 0, sticky = 'nsew')
    bar_v.grid(column = 1, row = 0, sticky = 'ns')
    bar_h.grid(column = 0, row = 1, sticky = 'ew')

    right_down.grid_rowconfigure(0, weight = 12)

    #--------------------------------------------
    # 1.5 - Configurando alinhamento e tamanho:
    #--------------------------------------------

    alignment = ["center", "center", "center", "center", "nw"]
    size = [30, 120, 165, 165, 200]
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

    #-------------------------------------------------
    # 2.1 - Pega os valores dos campos
    #-------------------------------------------------

    date = e_date.get()
    entry_time = e_entry_time.get()
    exit_time = e_exit_time.get()
    observation = e_observation.get()

    #-----------------------------------------------------
    # 2.2 - Armazena os valores dos campos em uma lista
    #-----------------------------------------------------

    array = [date, entry_time, exit_time, observation]

    #-----------------------------------------------------
    # 2.3 - Realiza as condições de um campo vazio
    #-----------------------------------------------------

    if date == '' or entry_time == '' or exit_time == '':
        messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
    else:
        crud.insert_info(array)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        #-----------------------------------------------------
        # 2.4 - Exclui os valores no campo
        #-----------------------------------------------------

        e_date.delete(0, 'end')
        e_entry_time.delete(0, 'end')
        e_exit_time.delete(0, 'end')
        e_observation.delete(0, 'end')
    
    #-------------------------------------------------------------
    # 2.5 - Exclui a antiga tabela e visualizamos ela atualizada
    #-------------------------------------------------------------

    for widget in right_down.winfo_children():
        widget.destroy()

    show_table()

#-------------------------------------------------
# 3 - Atualizar os dados no banco de dados e tabela 
#-------------------------------------------------

def update():
    try:
        #-------------------------------------------------
        # 3.1 - Retorna os valores da tabela como lista
        #------------------------------------------------- 

        table_data = table.focus()
        table_dictionary = table.item(table_data)
        table_list = table_dictionary['values']

        #-------------------------------------------------
        # 3.2 - Retorna o ID
        #------------------------------------------------- 

        value_id = table_list[0]
        
        #-------------------------------------------------
        # 3.3 - Deleta os valores dos campos (caso haja)
        #------------------------------------------------- 

        e_date.delete(0, 'end')
        e_entry_time.delete(0, 'end')
        e_exit_time.delete(0, 'end')
        e_observation.delete(0, 'end')

        #-------------------------------------------------
        # 3.4 - Insere os valores da tabela nos campo
        #------------------------------------------------- 

        e_date.insert(0, table_list[1])
        e_entry_time.insert(0, table_list[2])
        e_exit_time.insert(0, table_list[3])
        e_observation.insert(0, table_list[4])

        #-------------------------------------------------
        # 3.5 - Atualiza os dados
        #------------------------------------------------- 

        def update_data():

            #-------------------------------------------------
            # 3.5.1 - Pega os valores dos campos
            #-------------------------------------------------

            date = e_date.get()
            entry_time = e_entry_time.get()
            exit_time = e_exit_time.get()
            observation = e_observation.get()

            #-----------------------------------------------------
            # 3.5.2 - Armazena os valores dos campos em uma lista
            #-----------------------------------------------------

            array = [date, entry_time, exit_time, observation, value_id]

            #-----------------------------------------------------
            # 3.5.3 - Realiza as condições de um campo vazio
            #-----------------------------------------------------

            if date == '' or entry_time == '' or exit_time == '':
                messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
            else:
                crud.update_info(array)
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

                #-----------------------------------------------------
                # 3.5.4 - Exclui os valores no campo
                #-----------------------------------------------------

                e_date.delete(0, 'end')
                e_entry_time.delete(0, 'end')
                e_exit_time.delete(0, 'end')
                e_observation.delete(0, 'end')
            
            #-------------------------------------------------------------
            # 3.5.5 - Exclui a antiga tabela e visualizamos ela atualizada
            #-------------------------------------------------------------

            for widget in right_down.winfo_children():
                widget.destroy()

            show_table()

        #-------------------------------------------------
        # 3.6 - Criando e configurando botão 'Confirmar'
        #-------------------------------------------------

        b_confirm = tk.Button(left_down, command = update_data, text = 'Confirmar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
        b_confirm.place(x = 115, y = 350)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

#-------------------------------------------------
# 4 - Deleta os dados no banco de dados e tabela 
#-------------------------------------------------

def delete():
    try:
        #-------------------------------------------------
        # 4.1 - Retorna os valores da tabela como lista
        #------------------------------------------------- 

        table_data = table.focus()
        table_dictionary = table.item(table_data)
        table_list = table_dictionary['values']

        #-------------------------------------------------
        # 4.2 - Retorna o ID como lista
        #------------------------------------------------- 

        value_id = [table_list[0]]

        #-------------------------------------------------
        # 4.3 - Deleta dados da tabela
        #------------------------------------------------- 

        crud.delete_info(value_id)
        messagebox.showinfo('Deletados', 'Os dados foram deletados com sucesso!')

        #-------------------------------------------------------------
        # 3.5.5 - Exclui a antiga tabela e visualizamos ela atualizada
        #-------------------------------------------------------------

        for widget in right_down.winfo_children():
            widget.destroy()

        show_table()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


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
windows.geometry('990x453')
windows.configure(background = co9)
windows.resizable(width = False, height = False)

#--------------------------------------------
# Dividindo janela: 
#--------------------------------------------

left_top = tk.Frame(windows, width = 310, height = 50, background = co2, relief = 'flat')
left_top.grid(row = 0, column = 0)

left_down = tk.Frame(windows, width = 310, height = 403, background = co1, relief = 'flat')
left_down.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 0, pady = 1)

right_up = tk.Frame(windows, width = 588, height = 50, background = co1, relief = 'flat')
right_up.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

right_down = tk.Frame(windows, width = 588, height = 403, background = co1, relief = 'flat')
right_down.grid(row = 1, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

#--------------------------------------------
# Criando labels e entrys: 
#--------------------------------------------

#--------------------------------------------
# 1 - Criando titulo: 
#--------------------------------------------

app_name = tk.Label(left_top, text = 'Base de Horas - Pessoal', anchor = tk.NW, font = ('Ivy 13 bold'), background = co2, fg = co1, relief = 'flat')
app_name.place(x = 10, y = 20)

#--------------------------------------------
# 2 - Criando campo "Data":
#--------------------------------------------

l_date = tk.Label(left_down, text = 'Data do expediente: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_date.place(x = 10, y = 40)
e_date = DateEntry(left_down, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, data_patter = 'dd/mm/yyyy')
e_date.place(x = 160, y = 40)

#--------------------------------------------
# 3 - Criando campo "Horário de entrada":
#--------------------------------------------

l_entry_time = tk.Label(left_down, text = 'Horário de entrada: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_entry_time.place(x = 10, y = 100)
e_entry_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_entry_time.place(x = 160, y = 100)

#--------------------------------------------
# 4 - Criando campo "Horário de saida":
#--------------------------------------------

l_exit_time = tk.Label(left_down, text = 'Horário de saida: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_exit_time.place(x = 10, y = 160)
e_exit_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_exit_time.place(x = 160, y = 160)

#--------------------------------------------
# 5 - Criando campo "Observações":
#--------------------------------------------

l_observation = tk.Label(left_down, text = 'Observações: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_observation.place(x = 10, y = 220)
e_observation = tk.Entry(left_down, width = 35, justify = 'left', relief = 'solid')
e_observation.place(x = 15, y = 250)

#--------------------------------------------
# 6 - Criando campo "Filtro":
#--------------------------------------------

l_filter_data = tk.Label(right_up, text = 'Filtro: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_filter_data.place(x = 10, y = 20)
e_filter_data = tk.Entry(right_up, width = 15, justify = 'left', relief = 'solid')
e_filter_data.place(x = 75, y = 20)
    
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

b_update = tk.Button(left_down, command = update,text = 'Atualizar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
b_update.place(x = 115, y = 310)

#--------------------------------------------
# 3 - Criando botão "Deletar":
#--------------------------------------------

b_delete = tk.Button(left_down, text = 'Deletar', command = delete, width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
b_delete.place(x = 215, y = 310)

#--------------------------------------------
# 4 - Criando botão "Buscar":
#--------------------------------------------

b_search = tk.Button(right_up, text = 'Buscar', width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
b_search.place(x = 230, y = 20)

#--------------------------------------------
# Visualizando tabela: 
#--------------------------------------------

show_table()

#--------------------------------------------
# Mantendo o sistema em loop: 
#--------------------------------------------

windows.mainloop()