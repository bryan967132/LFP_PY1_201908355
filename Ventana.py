from logging import PlaceHolder
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from turtle import back
from Componentes import Componentes
from Analizador import AnalizadorLexico

class Inicio:
    def __init__(self):
        self.tokens = None

    def iniciar(self):
        self.raiz = tk.Tk()
        self.raiz.title('LFP - Práctica 1')
        self.raiz.resizable(0,0)
        self.raiz.geometry('700x500')
        self.raiz.config(bg = 'white')
        tk.Label(self.raiz,text = 'Menú',font = ('Comic Sans MS', 30),background='#0059b3',foreground = 'white').pack(fill = tk.X)
        self.areatexto = tk.Text(self.raiz,font = ('Comic Sans MS',11),width = 45,height = 12,borderwidth = 5,fg = '#0060B2')
        self.areatexto.place(x = 50,y = 100)
        
        tk.Button(self.raiz,text = 'Buscar Archivo',font = ('Comic Sans MS',12),width = 15,height = 2,borderwidth = 5,bg = '#8D2FB6',fg = 'white',activebackground = '#7219A7',activeforeground = 'white',command = self.chooseFile).place(x = 50,y = 375)
        tk.Button(self.raiz,text = 'Analizar',font = ('Comic Sans MS',12),width = 15,height = 2,borderwidth = 5,bg = '#107C41',fg = 'white',activebackground = '#107C41',activeforeground = 'white',command = self.analizar).place(x = 299,y = 375)

        tk.Label(self.raiz,text = 'Reportes',font = ('Comic Sans MS', 12),background = "white",foreground = '#0059b3').place(x = 510,y = 90)
        self.combo = ttk.Combobox(self.raiz,state = 'readonly',values = ['Reporte de Tokens','Reporte de Errores','Manual de Usuario','Manual Técnico'])
        self.combo.bind("<<ComboboxSelected>>",self.chooseReport)
        self.combo.place(x = 510, y = 125)

        self.raiz.mainloop()
    
    def chooseFile(self):
        try:
            archivo = askopenfilename()
            file = open(archivo).read()
            self.areatexto.delete('1.0','end')
            self.areatexto.insert(tk.INSERT,file)
        except:
            self.areatexto.delete('1.0','end')
    
    def analizar(self):
        contenido = self.areatexto.get('1.0','end').strip()
        if len(contenido) > 0:
            lexico = AnalizadorLexico()
            lexico.analizar(contenido)
            self.tokens = lexico.listaTokens
            if len(self.tokens) > 0:
                cmp = Componentes()
                componentes = cmp.getComponentes(self.tokens)
                print(componentes)
            else:
                tk.messagebox.showinfo(message = "Sin tokens detectados",title = "Tokens")
        else:
            tk.messagebox.showinfo(message = "No hay un archivo cargado",title = "Archivo")
    
    def chooseReport(self,event):
        reporte = self.combo.get()
        if reporte == 'Reporte de Tokens':
            print('Se hace el Reporte de Tokens en html')
        elif reporte == 'Reporte de Errores':
            print('Se hace el Reporte de Errores en html')
        elif reporte == 'Manual de Usuario':
            print('Se abre el Manual de Usuario')
        elif reporte == 'Manual Técnico':
            print('Se abre el Manual Técnico')