#------Importando bibliotecas------#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import locale
import crud

#---------Definindo_localização_pt-br---------#

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

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
co10 = '#ffbd03' # Amarelo
co11 = '#5783db' # Azul escuro

#---------Criando_software---------#

def ivy(): 

    #---------Criando_janela---------#

    windows = tk.Tk()
    windows.title('IVY - Criada por Brenno Kenji (testes)')
    windows.geometry('1000x463')
    windows.configure(background = co9)
    windows.resizable(width = False, height = False)

    #---------Criando_abas---------#

    guide = ttk.Notebook(windows)
    guide.place(x = 0, y = 0, height = 463, width = 1000)

    dashboard = tk.Frame(guide)
    guide.add(dashboard, text = 'Dashboard')

    hours = tk.Frame(guide)
    guide.add(hours, text = 'Controle de horas')

    activies = tk.Frame(guide)
    guide.add(activies, text = 'Controle de Atividades')

    social = tk.Frame(guide)
    guide.add(social, text = 'Fórum')

    #---------Criando_aba_controle_de_horas---------#

    def hours_management():

        #---------Funções---------#

        ##---------Visualizando_tabela_horas---------##
        
        def h_show_table():

            global h_table # Faz a variável local se tornar global

            ###---------Criando_titulos_tabela---------###

            coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

            ###---------Acessando_dados---------###

            data = crud.h_access_info()

            ###---------Criando_tabela---------###

            h_table = ttk.Treeview(h_right_down, selectmode = "extended", columns = coluna_header, show = "headings")
            bar_v = ttk.Scrollbar(h_right_down, orient = "vertical", command = h_table.yview)
            bar_h = ttk.Scrollbar(h_right_down, orient = "horizontal", command = h_table.xview)

            ###---------Visualizando_tabela---------###

            h_table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
            h_table.grid(column = 0, row = 0, sticky = 'nsew')
            bar_v.grid(column = 1, row = 0, sticky = 'ns')
            bar_h.grid(column = 0, row = 1, sticky = 'ew')

            h_right_down.grid_rowconfigure(0, weight = 12)

            ###---------Configurando_alinhamento_tamanho---------###

            alignment = ["center", "center", "center", "center", "nw"]
            size = [30, 120, 165, 165, 200]
            n = 0

            for col in coluna_header:
                h_table.heading(col, text = col.title(), anchor = tk.CENTER)
                h_table.column(col, width = size[n], anchor = alignment[n])
                
                n += 1

            for item in data:
                h_table.insert('', 'end', values = item)
        
        def h_insert():

            ###---------Pega_valor---------###

            date = h_e_date.get()
            entry_time = h_e_entry_time.get()
            exit_time = h_e_exit_time.get()
            observation = h_e_observation.get()

            ###---------Armazena_dados---------###

            array = [date, entry_time, exit_time, observation]

            ###---------Condições---------###

            if date == '' or entry_time == '' or exit_time == '':
                messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
            else:
                crud.h_insert_info(array)
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

                ####---------Exclui_valores---------####

                h_e_date.delete(0, 'end')
                h_e_entry_time.delete(0, 'end')
                h_e_exit_time.delete(0, 'end')
                h_e_observation.delete(0, 'end')
            
            ###---------Tabela_atualizada---------###

            for widget in h_right_down.winfo_children():
                widget.destroy()

            h_show_table()

        def h_update():
            try:
                ###---------Retorna_valores_como_lista---------###

                table_data = h_table.focus()
                table_dictionary = h_table.item(table_data)
                table_list = table_dictionary['values']

                ###---------Retorna_ID---------###

                value_id = table_list[0]
                
                ###---------Deleta_valores---------###

                h_e_date.delete(0, 'end')
                h_e_entry_time.delete(0, 'end')
                h_e_exit_time.delete(0, 'end')
                h_e_observation.delete(0, 'end')

                ###---------Inseri_valores_nos_campos---------###

                h_e_date.insert(0, table_list[1])
                h_e_entry_time.insert(0, table_list[2])
                h_e_exit_time.insert(0, table_list[3])
                h_e_observation.insert(0, table_list[4])

                ###---------Atualiza_dados---------###

                def update_data():

                    ####---------Pega_valor---------####

                    date = h_e_date.get()
                    entry_time = h_e_entry_time.get()
                    exit_time = h_e_exit_time.get()
                    observation = h_e_observation.get()

                    ####---------Armazena_dados---------####

                    array = [date, entry_time, exit_time, observation, value_id]

                    ####---------Condições---------####

                    if date == '' or entry_time == '' or exit_time == '':
                        messagebox.showerror('Erro', 'A data e os horários são campos obrigatórios')
                    else:
                        crud.h_update_info(array)
                        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

                        #####---------Exclui_valores---------#####

                        h_e_date.delete(0, 'end')
                        h_e_entry_time.delete(0, 'end')
                        h_e_exit_time.delete(0, 'end')
                        h_e_observation.delete(0, 'end')
                    
                    ####---------Tabela_atualizada---------####

                    for widget in h_right_down.winfo_children():
                        widget.destroy()

                    h_show_table()

                ###---------Configura_botão_confirmar---------###

                b_confirm = tk.Button(h_left_down, command = update_data, text = 'Confirmar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
                b_confirm.place(x = 115, y = 350)

            except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
        
        def h_delete():
            try:
                ###---------Retorna_valores_como_lista---------###

                table_data = h_table.focus()
                table_dictionary = h_table.item(table_data)
                table_list = table_dictionary['values']

                ###---------Retorna_ID---------###

                value_id = [table_list[0]]

                ###---------Deleta_dados---------###

                crud.h_delete_info(value_id)
                messagebox.showinfo('Deletados', 'Os dados foram deletados com sucesso!')

                ###---------Tabela_atualizada---------###

                for widget in h_right_down.winfo_children():
                    widget.destroy()

                h_show_table()

            except IndexError:
                messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        def h_filter_date():
            try:
                ###---------Filtra_tabela---------###

                for widget in h_right_down.winfo_children():
                    widget.destroy()
                
                ###---------Pega_valor---------###

                filter_entry = h_e_filter_date_entry.get()
                filter_exit = h_e_filter_date_exit.get()

                ###---------Armazena_dados---------###

                date = [filter_entry, filter_exit]

                ###---------Filtra_data---------###

                filtered_data = crud.h_select_date(date)
                messagebox.showinfo('Filtrado', f'Foi filtrado as datas entre {filter_entry} até {filter_exit}.')

                ###---------Tabela_atualizada---------###

                coluna_header = ['ID', 'Data', 'Horário de entrada', 'Horário de saida', 'Observações']

                h_table = ttk.Treeview(h_right_down, selectmode = "extended", columns = coluna_header, show = "headings")
                bar_v = ttk.Scrollbar(h_right_down, orient = "vertical", command = h_table.yview)
                bar_h = ttk.Scrollbar(h_right_down, orient = "horizontal", command = h_table.xview)

                h_table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
                h_table.grid(column = 0, row = 0, sticky = 'nsew')
                bar_v.grid(column = 1, row = 0, sticky = 'ns')
                bar_h.grid(column = 0, row = 1, sticky = 'ew')

                h_right_down.grid_rowconfigure(0, weight = 12)

                alignment = ["center", "center", "center", "center", "nw"]
                size = [30, 120, 165, 165, 200]
                n = 0

                for col in coluna_header:
                    h_table.heading(col, text = col.title(), anchor = tk.CENTER)
                    h_table.column(col, width = size[n], anchor = alignment[n])
                    
                    n += 1

                for item in filtered_data:
                    h_table.insert('', 'end', values = item)

            except IndexError:
                messagebox.showerror('Erro', 'Seleciona uma data para realizar a filtragem')
                
        #---------Variáveis_globais---------#

        global h_table 
        global h_left_top
        global h_left_down
        global h_right_up
        global h_right_down
        global h_app_name
        global h_l_date
        global h_e_date
        global h_l_entry_time
        global h_e_entry_time
        global h_l_exit_time
        global h_e_exit_time
        global h_l_observation
        global h_e_observation
        global h_l_filter_date_entry
        global h_e_filter_date_entry
        global h_l_filter_date_exit
        global h_e_filter_date_exit

        #---------Dividindo_janela---------#

        h_left_top = tk.Frame(hours, width = 310, height = 50, background = co2, relief = 'flat')
        h_left_top.grid(row = 0, column = 0)

        h_left_down = tk.Frame(hours, width = 310, height = 403, background = co1, relief = 'flat')
        h_left_down.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 0, pady = 1)

        h_right_up = tk.Frame(hours, width = 588, height = 50, background = co1, relief = 'flat')
        h_right_up.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

        h_right_down = tk.Frame(hours, width = 588, height = 403, background = co1, relief = 'flat')
        h_right_down.grid(row = 1, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

        #---------Criando_Labels_e_Entrys---------#

        ##---------Criando_Titulo---------##

        h_app_name = tk.Label(h_left_top, text = 'Controle de Horas', anchor = tk.NW, font = ('Ivy 13 bold'), background = co2, fg = co1, relief = 'flat')
        h_app_name.place(x = 10, y = 20)

        ##---------Criando_campo_"Data do expediente"---------##

        h_l_date = tk.Label(h_left_down, text = 'Data do expediente: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_date.place(x = 10, y = 40)
        h_e_date = DateEntry(h_left_down, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
        h_e_date.place(x = 160, y = 40)

        ##---------Criando_campo_"Horário de entrada"---------##

        h_l_entry_time = tk.Label(h_left_down, text = 'Horário de entrada: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_entry_time.place(x = 10, y = 100)
        h_e_entry_time = tk.Entry(h_left_down, width = 15, justify = 'left', relief = 'solid')
        h_e_entry_time.place(x = 160, y = 100)

        ##---------Criando_campo_"Horário de saida"---------##

        h_l_exit_time = tk.Label(h_left_down, text = 'Horário de saida: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_exit_time.place(x = 10, y = 160)
        h_e_exit_time = tk.Entry(h_left_down, width = 15, justify = 'left', relief = 'solid')
        h_e_exit_time.place(x = 160, y = 160)

        ##---------Criando_campo_"Observações"---------##

        h_l_observation = tk.Label(h_left_down, text = 'Observações: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_observation.place(x = 10, y = 220)
        h_e_observation = tk.Entry(h_left_down, width = 35, justify = 'left', relief = 'solid')
        h_e_observation.place(x = 15, y = 250)

        ##---------Criando_campo_"Filtrar data"---------##

        h_l_filter_date_entry = tk.Label(h_right_up, text = 'Filtrar data de: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_filter_date_entry.place(x = 10, y = 20)
        h_e_filter_date_entry = DateEntry(h_right_up, width = 12, justify = 'left', relief = 'solid', locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
        h_e_filter_date_entry.place(x = 130, y = 20)

        h_l_filter_date_exit = tk.Label(h_right_up, text = 'a', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        h_l_filter_date_exit.place(x = 252, y = 20) 
        h_e_filter_date_exit = DateEntry(h_right_up, width = 12, justify = 'left', relief = 'solid', locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
        h_e_filter_date_exit.place(x = 275, y = 20) 
            
        #---------Criando_Botões---------#

        ##---------Criando_botão_"Inserir"---------##

        h_b_input = tk.Button(h_left_down, command = h_insert, text = 'Inserir', width = 7, font = ('Ivy 8 bold'), background = co6, fg = co1, relief = 'raised', overrelief = 'ridge')
        h_b_input.place(x = 15, y = 310)

        ##---------Criando_botão_"Atualizar"---------##

        h_b_update = tk.Button(h_left_down, command = h_update, text = 'Atualizar', width = 7, font = ('Ivy 8 bold'), background = co2, fg = co1, relief = 'raised', overrelief = 'ridge')
        h_b_update.place(x = 115, y = 310)

        ##---------Criando_botão_"Deletar"---------##

        h_b_delete = tk.Button(h_left_down, text = 'Deletar', command = h_delete, width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
        h_b_delete.place(x = 215, y = 310)

        ##---------Criando_botão_"Buscar"---------##

        h_b_search = tk.Button(h_right_up, text = 'Buscar', command = h_filter_date, width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
        h_b_search.place(x = 420, y = 20)

        ##---------Criando_botão_"Retirar Filtro"---------##

        h_b_search = tk.Button(h_right_up, text = 'Retirar Filtro', command = h_show_table, width = 10, font = ('Ivy 8 bold'), background = co6, fg = co1, relief = 'raised', overrelief = 'ridge')
        h_b_search.place(x = 520, y = 20)

        #---------Visualizar_tabela---------#

        h_show_table()

    #---------Criando_aba_controle_de_atividades---------#

    def activies_management():

        #---------Funções---------#

        ##---------Visualizando_tabela_atividades---------##
        
        def a_show_table():

            global a_table
            
            coluna_header = ['Data', 'Atividade', 'Descriçao', 'Progresso (%)']

            data = crud.a_access_info()

            a_table = ttk.Treeview(a_right_down, selectmode = "extended", columns = coluna_header, show = "headings")
            bar_v = ttk.Scrollbar(a_right_down, orient = "vertical", command = a_table.yview)
            bar_h = ttk.Scrollbar(a_right_down, orient = "horizontal", command = a_table.xview)   

            a_table.configure(yscrollcommand = bar_v.set, xscrollcommand = bar_h.set)
            a_table.grid(column = 0, row = 0, sticky = 'nsew')
            bar_v.grid(column = 1, row = 0, sticky = 'ns')
            bar_h.grid(column = 0, row = 1, sticky = 'ew')

            a_right_down.grid_rowconfigure(0, weight = 12)

            alignment = ["center", "nw", "nw", "center"]
            size = [120, 140, 290, 120]
            n = 0

            for col in coluna_header:
                a_table.heading(col, text = col.title(), anchor = tk.CENTER)
                a_table.column(col, width = size[n], anchor = alignment[n])
                
                n += 1

            for item in data:
                a_table.insert('', 'end', values = item)

        #---------Variáveis_globais---------#

        global a_left_top
        global a_left_down
        global a_right_up
        global a_right_down
        global a_app_name

        #---------Dividindo_janela---------#

        a_left_top = tk.Frame(activies, width = 310, height = 50, background = co2, relief = 'flat')
        a_left_top.grid(row = 0, column = 0)

        a_left_down = tk.Frame(activies, width = 310, height = 403, background = co1, relief = 'flat')
        a_left_down.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 0, pady = 1)

        a_right_up = tk.Frame(activies, width = 690, height = 50, background = co1, relief = 'flat')
        a_right_up.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

        a_right_down = tk.Frame(activies, width = 690, height = 403, background = co1, relief = 'flat')
        a_right_down.grid(row = 1, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = tk.NSEW)

        #---------Criando_Labels_e_Entrys---------#

        ##---------Criando_Titulo---------##

        a_app_name = tk.Label(a_left_top, text = 'Controle de Atividades', anchor = tk.CENTER, font = ('Ivy 13 bold'), background = co2, fg = co1, relief = 'flat')
        a_app_name.place(x = 10, y = 20)

        ##---------Criando_data---------##

        a_l_date = tk.Label(a_left_down, text = 'Data da atividade: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        a_l_date.place(x = 10, y = 20)
        a_e_date = DateEntry(a_left_down, width = 14, background = 'darkblue', foreground = 'white', borderwidth = 2, locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
        a_e_date.place(x = 160, y = 20)

        ##---------Criando_tipo_de_atividade---------##

        list_type = ['exemplo1', 'exemplo2', 'exemplo3']
        
        a_l_type = tk.Label(a_left_down, text = 'Tipo de atividade: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        a_l_type.place(x = 10, y = 80)
        a_e_type = ttk.Combobox(a_left_down, values = list_type, width = 14, background = 'darkblue', foreground = co4)
        a_e_type.set(list_type[1])
        a_e_type.place(x = 160, y = 80)
        
        ##---------Criando_detalhe_da_atividade---------##

        a_l_type_details = tk.Label(a_left_down, text = 'Detalhe da atividade(s): ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        a_l_type_details.place(x = 10, y = 130)
        a_e_type_details = tk.Entry(a_left_down, width = 35, justify = 'left', relief = 'solid')
        a_e_type_details.place(x = 10, y = 170)


        ##---------Criando_barra_de_progressão---------##

        prog_bar = tk.DoubleVar()
        prog_bar.set(0)
        
        prog_values =[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
        def update_progressbar():
            value_bar_progress = int(a_e_progress.get())
            prog_bar.set(value_bar_progress)
    
        a_l_progress = tk.Label(a_left_down, text = 'Progressão (%): ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        a_l_progress.place(x = 10, y = 230)
        a_e_progress = ttk.Spinbox(a_left_down, values = prog_values, command = update_progressbar, width = 14, background = 'darkblue', foreground = co4)
        a_e_progress.place(x = 155, y = 230)

        a_bar_progress = ttk.Progressbar(a_left_down, variable = prog_bar, maximum = 100, length = 280)
        a_bar_progress.place(x = 10, y = 290)

        #---------Criando_Botões---------#
        
        ##---------Botão_Adicionar---------##

        a_b_add_activies = tk.Button(a_left_down, text = 'Adicionar', width = 7, font = ('Ivy 8 bold'), background = co11, fg = co1, relief = 'raised', overrelief = 'ridge')
        a_b_add_activies.place(x = 10, y = 320)

        ##---------Botão_Editar---------##

        a_b_edit = tk.Button(a_left_down, text = 'Editar', width = 7, font = ('Ivy 8 bold'), background = co10, fg = co1, relief = 'raised', overrelief = 'ridge')
        a_b_edit.place(x = 110, y = 320)

        ##---------Botão_Excluir---------##

        a_b_delete = tk.Button(a_left_down, text = 'Excluir', width = 7, font = ('Ivy 8 bold'), background = co7, fg = co1, relief = 'raised', overrelief = 'ridge')
        a_b_delete.place(x = 210, y = 320)

        a_show_table()
        
    #---------Chamando_funções---------#

    hours_management()
    activies_management()

    #---------Manter_o_sistema_em_loop---------#

    windows.mainloop()

#---------Rodando_o_sistema---------#

if __name__ == '__main__':
    ivy()