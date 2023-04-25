from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import pyttsx3
from PyPDF2 import PdfReader 

global engine
engine = pyttsx3.init()

def escolha():
    global filename

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=(('PDFs','*.pdf'),
        ('All files', '*.*')))
    nome = ttk.Label(janela,text=filename)
    nome.grid(column=0,row=2,columnspan=2)
    
    
    
    
def leitor():
    escolha_arquivo = filename
    engine.setProperty('rate', 130)
    pdf_file = open(escolha_arquivo,'rb')
    pdf_reader = PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        engine.say(text)
        engine.runAndWait()
    pdf_file.close()
    messagebox.showinfo("Aviso", "Texto lido")
        






janela = Tk()
janela.geometry('600x400')
lbesolha = ttk.Label(janela,text='Escolha um arquivo')
btnescolha = ttk.Button(janela,text='Abrir',command=escolha)
btnleitura = ttk.Button(janela,text='Play',command=leitor)


lbesolha.grid(column=0,row=0)
btnescolha.grid(column=1,row=0)
btnleitura.grid(column=0,row=1)


janela.mainloop()