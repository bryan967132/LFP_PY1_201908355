import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from Componentes import Componentes
from Analizador import AnalizadorLexico
from Reportes import Reportes
from Formulario import Formulario

class Inicio:
    def __init__(self):
        self.tokens = None
        self.errores = None

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
            self.tokens = None
            self.errores = None
        except:
            self.areatexto.delete('1.0','end')
    
    def analizar(self):
        contenido = self.areatexto.get('1.0','end').strip()
        if len(contenido) > 0:
            lexico = AnalizadorLexico()
            lexico.analizar(contenido)
            self.tokens = lexico.listaTokens
            self.errores = lexico.listaErrores
            if len(self.tokens) > 0:
                cmp = Componentes()
                componentes = cmp.getComponentes(self.tokens)
                Formulario().generar(componentes,contenido)
            else:
                tk.messagebox.showinfo(message = "Sin tokens detectados",title = "Tokens")
        else:
            tk.messagebox.showinfo(message = "No hay un archivo cargado",title = "Archivo")
    
    def chooseReport(self,event):
        reporte = self.combo.get()
        if reporte == 'Manual de Usuario':
            print('Se abre el Manual de Usuario')
        elif reporte == 'Manual Técnico':
            print('Se abre el Manual Técnico')
        else:
            contenido = self.areatexto.get('1.0','end').strip()
            if len(contenido) > 0:
                if reporte == 'Reporte de Tokens':
                    if self.tokens:
                        Reportes().repTokens(self.tokens)
                    else:
                        tk.messagebox.showinfo(message = "No se encontraron tokens",title = "Análisis")
                elif reporte == 'Reporte de Errores':
                    if self.errores:
                        Reportes().repErrores(self.errores)
                    else:
                        tk.messagebox.showinfo(message = "No se encontraron errores",title = "Análisis")
            else:
                tk.messagebox.showinfo(message = "No hay un archivo cargado",title = "Archivo")
        
        