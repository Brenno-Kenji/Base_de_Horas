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

def login():
    windows = tk.Tk()
    windows.title('Área de cadastro - Ivy')
    windows.geometry('1000x463')
    windows.configure(background = co9)
    windows.resizable(width = False, height = False)

    windows.mainloop()

    def login_area():
        pass

    def new_acount():
        pass

if __name__ == '__main__':
    login()