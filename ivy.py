#------Importando bibliotecas------#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import locale
import crud

#---------Definindo_localização_pt-br---------#

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

#---------Variáveis_globais---------#

global table #O valor da variável table é retornado como global

#---------Funções---------#

##---------Visualizando_tabela---------##

def show_table():

    global table # Faz a variável local se tornar local

    ###---------Criando_titulos_tabela---------###

    coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

    ###---------Acessando_dados---------###

    data = crud.access_info()

    ###---------Criando_tabela---------###

    table = ttk.Treeview(right_down, selectmode = "extended", columns = coluna_header, show = "headings")
    bar_v = ttk.Scrollbar(right_down, orient = "vertical", command = table.yview)
    bar_h = ttk.Scrollbar(right_down, orient = "horizontal", command = table.xview)

    ###---------Visualizando_tabela---------###

    table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
    table.grid(column = 0, row = 0, sticky = 'nsew')
    bar_v.grid(column = 1, row = 0, sticky = 'ns')
    bar_h.grid(column = 0, row = 1, sticky = 'ew')

    right_down.grid_rowconfigure(0, weight = 12)

    ###---------Configurando_alinhamento_tamanho---------###

    alignment = ["center", "center", "center", "center", "nw"]
    size = [30, 120, 165, 165, 200]
    n = 0

    for col in coluna_header:
        table.heading(col, text = col.title(), anchor = tk.CENTER)
        table.column(col, width = size[n], anchor = alignment[n])
        
        n += 1

    for item in data:
        table.insert('', 'end', values = item)

##---------Insere_dados ---------##

def insert():

    ###---------Pega_valor---------###

    date = e_date.get()
    entry_time = e_entry_time.get()
    exit_time = e_exit_time.get()
    observation = e_observation.get()

    ###---------Armazena_dados---------###

    array = [date, entry_time, exit_time, observation]

    ###---------Condições---------###

    if date == '' or entry_time == '' or exit_time == '':
        messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
    else:
        crud.insert_info(array)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        ####---------Exclui_valores---------####

        e_date.delete(0, 'end')
        e_entry_time.delete(0, 'end')
        e_exit_time.delete(0, 'end')
        e_observation.delete(0, 'end')
    
    ###---------Tabela_atualizada---------###

    for widget in right_down.winfo_children():
        widget.destroy()

    show_table()

##---------Atualiza_tabela---------##

def update():
    try:
        ###---------Retorna_valores_como_lista---------###

        table_data = table.focus()
        table_dictionary = table.item(table_data)
        table_list = table_dictionary['values']

        ###---------Retorna_ID---------###

        value_id = table_list[0]
        
        ###---------Deleta_valores---------###

        e_date.delete(0, 'end')
        e_entry_time.delete(0, 'end')
        e_exit_time.delete(0, 'end')
        e_observation.delete(0, 'end')

        ###---------Inseri_valores_nos_campos---------###

        e_date.insert(0, table_list[1])
        e_entry_time.insert(0, table_list[2])
        e_exit_time.insert(0, table_list[3])
        e_observation.insert(0, table_list[4])

        ###---------Atualiza_dados---------###

        def update_data():

            ####---------Pega_valor---------####

            date = e_date.get()
            entry_time = e_entry_time.get()
            exit_time = e_exit_time.get()
            observation = e_observation.get()

            ####---------Armazena_dados---------####

            array = [date, entry_time, exit_time, observation, value_id]

            ####---------Condições---------####

            if date == '' or entry_time == '' or exit_time == '':
                messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
            else:
                crud.update_info(array)
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

                #####---------Exclui_valores---------#####

                e_date.delete(0, 'end')
                e_entry_time.delete(0, 'end')
                e_exit_time.delete(0, 'end')
                e_observation.delete(0, 'end')
            
            ####---------Tabela_atualizada---------####

            for widget in right_down.winfo_children():
                widget.destroy()

            show_table()

        ###---------Configura_botão_confirmar---------###

        b_confirm = tk.Button(left_down, command = update_data, text = 'Confirmar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
        b_confirm.place(x = 115, y = 350)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

##---------Deleta_dados---------##

def delete():
    try:
        ###---------Retorna_valores_como_lista---------###

        table_data = table.focus()
        table_dictionary = table.item(table_data)
        table_list = table_dictionary['values']

        ###---------Retorna_ID---------###

        value_id = [table_list[0]]

        ###---------Deleta_dados---------###

        crud.delete_info(value_id)
        messagebox.showinfo('Deletados', 'Os dados foram deletados com sucesso!')

        ###---------Tabela_atualizada---------###

        for widget in right_down.winfo_children():
            widget.destroy()

        show_table()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

##---------Filtra_data---------##

def filter_date():
    try:
        ###---------Filtra_tabela---------###

        for widget in right_down.winfo_children():
            widget.destroy()
        
        ###---------Pega_valor---------###

        filter_entry = e_filter_date_entry.get()
        filter_exit = e_filter_date_exit.get()

        ###---------Armazena_dados---------###

        date = [filter_entry, filter_exit]

        ###---------Filtra_data---------###

        filtered_data = crud.select_date(date)
        messagebox.showinfo('Filtrado', f'Foi filtrado as datas entre {filter_entry} até {filter_exit}.')

        ###---------Tabela_atualizada---------###

        coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

        table = ttk.Treeview(right_down, selectmode = "extended", columns = coluna_header, show = "headings")
        bar_v = ttk.Scrollbar(right_down, orient = "vertical", command = table.yview)
        bar_h = ttk.Scrollbar(right_down, orient = "horizontal", command = table.xview)

        table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
        table.grid(column = 0, row = 0, sticky = 'nsew')
        bar_v.grid(column = 1, row = 0, sticky = 'ns')
        bar_h.grid(column = 0, row = 1, sticky = 'ew')

        right_down.grid_rowconfigure(0, weight = 12)

        alignment = ["center", "center", "center", "center", "nw"]
        size = [30, 120, 165, 165, 200]
        n = 0

        for col in coluna_header:
            table.heading(col, text = col.title(), anchor = tk.CENTER)
            table.column(col, width = size[n], anchor = alignment[n])
            
            n += 1

        for item in filtered_data:
            table.insert('', 'end', values = item)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona uma data para realizar a filtragem')

#---------Definindo_cores---------#

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

#---------Criando_janela---------#

windows = tk.Tk()
windows.title('Ferramente de base de horas - Criada por Brenno Kenji (versão: 0.2)')
windows.geometry('990x453')
windows.configure(background = co9)
windows.resizable(width = False, height = False)

#---------Dividindo_janela---------#

left_top = tk.Frame(windows, width = 310, height = 50, background = co2, relief = 'flat')
left_top.grid(row = 0, column = 0)

left_down = tk.Frame(windows, width = 310, height = 403, background = co1, relief = 'flat')
left_down.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 0, pady = 1)

right_up = tk.Frame(windows, width = 588, height = 50, background = co1, relief = 'flat')
right_up.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

right_down = tk.Frame(windows, width = 588, height = 403, background = co1, relief = 'flat')
right_down.grid(row = 1, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

#---------Criando_Labels_e_Entrys---------#

##---------Criando_Titulo---------##

app_name = tk.Label(left_top, text = 'Base de Horas - Pessoal', anchor = tk.NW, font = ('Ivy 13 bold'), background = co2, fg = co1, relief = 'flat')
app_name.place(x = 10, y = 20)

##---------Criando_campo_"Data do expediente"---------##

l_date = tk.Label(left_down, text = 'Data do expediente: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_date.place(x = 10, y = 40)
e_date = DateEntry(left_down, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
e_date.place(x = 160, y = 40)

##---------Criando_campo_"Horário de entrada"---------##

l_entry_time = tk.Label(left_down, text = 'Horário de entrada: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_entry_time.place(x = 10, y = 100)
e_entry_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_entry_time.place(x = 160, y = 100)

##---------Criando_campo_"Horário de saida"---------##

l_exit_time = tk.Label(left_down, text = 'Horário de saida: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_exit_time.place(x = 10, y = 160)
e_exit_time = tk.Entry(left_down, width = 15, justify = 'left', relief = 'solid')
e_exit_time.place(x = 160, y = 160)

##---------Criando_campo_"Observações"---------##

l_observation = tk.Label(left_down, text = 'Observações: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_observation.place(x = 10, y = 220)
e_observation = tk.Entry(left_down, width = 35, justify = 'left', relief = 'solid')
e_observation.place(x = 15, y = 250)

##---------Criando_campo_"Filtrar data"---------##

l_filter_date_entry = tk.Label(right_up, text = 'Filtrar data de: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_filter_date_entry.place(x = 10, y = 20)
e_filter_date_entry = DateEntry(right_up, width = 12, justify = 'left', relief = 'solid', locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
e_filter_date_entry.place(x = 130, y = 20)

l_filter_date_exit = tk.Label(right_up, text = 'a', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
l_filter_date_exit.place(x = 252, y = 20) 
e_filter_date_exit = DateEntry(right_up, width = 12, justify = 'left', relief = 'solid', locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
e_filter_date_exit.place(x = 275, y = 20) 
    
#---------Criando_Botões---------#

##---------Criando_botão_"Inserir"---------##

b_input = tk.Button(left_down, command = insert, text = 'Inserir', width = 7, font = ('Ivy 8 bold'), background = co6, fg = co1, relief = 'raised', overrelief = 'ridge')
b_input.place(x = 15, y = 310)

##---------Criando_botão_"Atualizar"---------##

b_update = tk.Button(left_down, command = update, text = 'Atualizar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
b_update.place(x = 115, y = 310)

##---------Criando_botão_"Deletar"---------##

b_delete = tk.Button(left_down, text = 'Deletar', command = delete, width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
b_delete.place(x = 215, y = 310)

##---------Criando_botão_"Buscar"---------##

b_search = tk.Button(right_up, text = 'Buscar', command = filter_date, width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
b_search.place(x = 420, y = 20)

##---------Criando_botão_"Retirar Filtro"---------##

b_search = tk.Button(right_up, text = 'Retirar Filtro', command = show_table, width = 10, font = ('Ivy 8 bold'), background = co6, fg = co1, relief = 'raised', overrelief = 'ridge')
b_search.place(x = 520, y = 20)

#---------Visualizar_tabela---------#

show_table()

#---------Manter_o_sistema_em_loop---------#

windows.mainloop()