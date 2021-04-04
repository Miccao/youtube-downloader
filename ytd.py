from pytube import YouTube
import os
from tkinter import *

root = Tk()
root.geometry('600x200')
root.title(':: Baixe do YouTube ::')


Label1 = Label(root, text='Insira o link do vídeo aqui:', font=('bold', 20))
Label1.place(x=120, y=20)

linkselecionado = StringVar()
link = Entry(root, width=60, textvariable=linkselecionado)
link.place(x=120, y=80)


# Comando chamado pelo botão para baixar o vídeo
def BaixarVideo():
    x= str(linkselecionado.get())
    ytvideo = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./videos'):
        os.makedirs('./videos')
    ytvideo.download('./videos')


Button(root, text="Baixar Vídeo", width=20, bg='red', fg='white', command=BaixarVideo).place(x=220, y=110)

root.mainloop()