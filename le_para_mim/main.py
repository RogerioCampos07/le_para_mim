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
    nome = ttk.Label(janela,text=f'Arquivo selecionado: {filename}')
    nome.place(x=10,y=100)
    
    
   
    
def leitor():
    escolha_arquivo = filename
    pdf_file = open(escolha_arquivo,'rb')
    pdf_reader = PdfReader(pdf_file)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice',voices[58].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-25)
    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        engine.say(text)
        engine.runAndWait()
    pdf_file.close()
    messagebox.showinfo("Aviso", "Texto lido")
    
        

janela = Tk()
janela.geometry('600x300')
janela.title('lê para mim')
frame_arquivo = ttk.LabelFrame(janela,relief='solid',text='Selecione um arquivo',padding=10,)
frame_botoes = ttk.Frame(janela,relief='solid',padding=10)
lbesolha = ttk.Label(frame_arquivo,text='Arquivo')
btnescolha = ttk.Button(frame_arquivo,text='Abrir',command=escolha)
btnleitura = ttk.Button(frame_botoes,text='Play',command=leitor)


frame_arquivo.place(x=10,y=40)
lbesolha.grid(column=0,row=0)
btnescolha.grid(column=1,row=0)
frame_botoes.place(x=10,y=170)
btnleitura.grid(column=0,row=0)


janela.mainloop()