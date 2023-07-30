#------Importando bibliotecas------#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import locale
import crud
import ivy

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

def login():
 
    #---------Criando_janela---------#

    windows = tk.Tk()
    windows.title('Área de cadastro - Ivy')
    windows.geometry('1000x465')
    windows.configure(background = co9)
    windows.resizable(width = False, height = False)

    #---------Criando_divisão---------#

    login = tk.Frame(windows, width = 400, height = 465, background = co1, relief = 'flat')
    login.grid(row = 0, column = 0, sticky = tk.NSEW, padx = 0, pady = 0)

    separator = ttk.Separator(windows, orient = 'vertical',  takefocus = 0)
    separator.grid(row = 0, column = 1, ipady = 500)

    new_login = tk.Frame(windows, width = 600, height = 465, background = co1, relief = 'flat')
    new_login.grid(row = 0, column = 2, sticky = tk.NSEW, padx = 0, pady = 0)

    #---------Area_de_login---------#

    def login_area():

        ##---------Titulo---------##

        f_title = tk.Frame(login, width = 400, height = 74, relief = 'flat')
        f_title.grid(row = 0, column = 0)

        l_title = tk.Label(f_title, text = 'Área de Login', font = 'Ivy 12 bold italic', fg = co4, relief = 'flat')
        l_title.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)        

        ##---------Campo_"E-mail"---------##

        f_email = tk.Frame(login, width = 400, height = 159, relief = 'flat')
        f_email.grid(row = 1, column = 0)

        l_email = tk.Label(f_email, text = 'Área de E-mail', font = 'Ivy 12 bold italic', fg = co4, relief = 'flat')
        l_email.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)   
        
        ##---------Campo_"Senha"---------##
        
        f_password = tk.Frame(login, width = 400, height = 158, relief = 'flat')
        f_password.grid(row = 2, column = 0)

        l_password = tk.Label(f_password, text = 'Área de Senha', font = 'Ivy 12 bold italic', fg = co4, relief = 'flat')
        l_password.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        ##---------Botão_"Login"---------##
   
        f_b_login = tk.Frame(login, width = 400, height = 74, relief = 'flat')
        f_b_login.grid(row = 3, column = 0)

        l_b_login = tk.Label(f_b_login, text = 'Área do botão', font = 'Ivy 12 bold italic', fg = co4, relief = 'flat')
        l_b_login.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        # h_l_date = tk.Label(h_left_down, text = 'Data do expediente: ', anchor = tk.NW, font = ('Ivy 9 bold'), background = co1, fg = co4, relief = 'flat')
        # h_l_date.place(x = 10, y = 40)
        # h_e_date = DateEntry(h_left_down, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, locale='pt_BR.utf8', data_patter = 'dd/mm/yyyy')
        # h_e_date.place(x = 160, y = 40)

    #---------Area_de_cadastro---------#

    def new_acount():
        pass

    login_area()
    new_acount()

    windows.mainloop()


if __name__ == '__main__':
    login()