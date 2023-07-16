#------Importando bibliotecas------#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import locale
import crud

# Realizando OOP:

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

class Ivy(tk.Tk):
    def __init__(self):

        #---------Criando_janela---------#

        super().__init__()
        self.title('Ferramente de base de horas - Criada por Brenno Kenji (versão: 0.2)')
        self.geometry('1000x463')
        self.configure(background = co9)
        self.resizable(width = False, height = False)
        
        #---------Dividindo_janela---------#

        guide = ttk.Notebook(self)
        guide.place(x = 0, y = 0, height = 463, width = 1000)

        dashboard = tk.Frame(guide)
        guide.add(dashboard, text = 'Dashboard')

        hours = tk.Frame(guide)
        guide.add(hours, text = 'Controle de horas')

        activies = tk.Frame(guide)
        guide.add(activies, text = 'Controle de Atividades')

        social = tk.Frame(guide)
        guide.add(social, text = 'Forúm')


if __name__ == '__main__':
    ivy = Ivy()
    ivy.mainloop()