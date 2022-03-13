import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *

class Inicio:
    def __init__(self):
        self.archivo = None
    
    def iniciar(self):
        self.raiz = tk.Tk()
        self.raiz.title("LFP - Práctica 1")
        self.raiz.resizable(0,0)
        self.raiz.geometry("700x500")
        self.raiz.config(bg = "light blue")
        titulo = tk.Label(self.raiz,text = "Menú",font = ("Comic Sans MS", 30),background="orange")
        titulo.pack(fill = tk.X)
        self.areatexto = tk.Text(self.raiz,font = ("Comic Sans MS",11),width = 45,height = 12)
        self.areatexto.place(x = 50,y = 100)
        
        tk.Button(self.raiz,text = "Buscar Archivo",font = ("Comic Sans MS",12),width = 15,height = 2,bg = "green",command = self.chooseFile).place(x = 50,y = 400)
        tk.Button(self.raiz,text = "Analizar",font = ("Comic Sans MS",12),width = 15,height = 2,bg = "orange",command = self.analizar).place(x = 250,y = 400)
        self.raiz.mainloop()
    
    def chooseFile(self):
        try:
            archivo = askopenfilename()
            file = open(archivo).read()
            self.areatexto = tk.Text(self.raiz,font = ("Comic Sans MS",11),width = 45,height = 12)
            self.areatexto.insert(tk.INSERT,file)
            self.areatexto.place(x = 50,y = 100)
        except:
            self.areatexto = tk.Text(self.raiz,font = ("Comic Sans MS",11),width = 45,height = 12)
            self.areatexto.insert(tk.INSERT,'')
            self.areatexto.place(x = 50,y = 100)
    
    def analizar(self):
        contenido = self.areatexto.get("1.0","end")
        if contenido != '\n':
            print(contenido)