#------Importando bibliotecas------#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkcalendar import Calendar, DateEntry
import locale
import crud

# Tipos de abas:

windows = tk.Tk()
windows.title('Teste')
windows.geometry('990x453')

windows.resizable(width = False, height = False)

nb = ttk.Notebook(windows) # cria o campo para as abas
nb.place(x = 0, y = 0, width = 990, height = 453)

tb1 = tk.Frame(nb)
nb.add(tb1, text = 'exemplo1') # adiciona um frame como aba

tb2 = tk.Frame(nb)
nb.add(tb2, text = 'exemplo2') 

b_input_1 = tk.Button(tb1, text = 'botao1')
b_input_1.place(x = 100, y = 50)

b_input_2 = tk.Button(tb2, text = 'botao2')
b_input_2.place(x = 100, y = 50)

windows.mainloop()

# guide = ttk.Notebook(windows)
# guide.place(x = 0, y = 0, height = 1000, width = 463)

# hours = tk.Frame(guide)
# guide.add(hours, text = 'Controle de horas')

