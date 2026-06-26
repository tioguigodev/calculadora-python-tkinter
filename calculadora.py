# Importar tkinter
from tkinter import*

# Importar math
import math

# cores
cor1 = '#3b3b3b'
cor2 = '#FFAB40'
cor3 = '#fffee3'
cor4 = '#ab2500'
cor5 = '#1e4226'
cor6 = '#ebe9e4'
cor7 = '#292929'

# Corpo do projeto
janela = Tk()
janela.title('Calculadora')
janela.geometry('350x450')
janela.resizable(False, False)
janela.config(bg=cor1)

# Tela digital
frame_tela = Frame(janela, width=350, height=150, bg=cor3)
frame_tela.grid(row=0, column=0)

# Corpo dos botões
frame_corpo = Frame(janela, width=350, height=450)
frame_corpo.grid(row=1, column=0)

# Criar variavel
tela = StringVar()
todas_entradas = ''

# Armazenar na variavel criada
app_label = Label(frame_tela, textvariable=tela, width=24, height=2, padx=7, bg=cor3, fg=cor5, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '))
app_label.place(x=0, y=80)

# Escrever na tela
def entrada(event):
    global todas_entradas
    todas_entradas = todas_entradas + str(event)
    tela.set(todas entradas)

# Botõe
b1 = Button(frame_corpo, text='C', width=5, height=2, bg=cor4, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, command = lambda: entrada('('), text='(', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=70, y=0)

b3 = Button(frame_corpo, command = lambda: entrada(')'), text=')', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=140, y=0)

b4 = Button(frame_corpo, command = lambda: entrada(str(math.pi)), text='π', width=5, height=2, bg=cor7,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=210, y=0)

b5 = Button(frame_corpo, text='⌫', width=5, height=2, bg=cor7,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=280, y=0)

b6 = Button(frame_corpo, command = lambda: entrada('7') ,text='7', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=0, y=60)

b7 = Button(frame_corpo, command = lambda: entrada('8'), text='8', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=70, y=60)

b8 = Button(frame_corpo, command = lambda: entrada('9'), text='9', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=140, y=60)

b9 = Button(frame_corpo, command = lambda: entrada('sqrt('), text='√', width=5, height=2, bg=cor4, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=210, y=60)

b10 = Button(frame_corpo, command = lambda: entrada('/'), text='÷', width=5, height=2, bg=cor4,fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=280, y=60)

b11 = Button(frame_corpo, command = lambda: entrada('4'), text='4', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=0, y=120)

b12 = Button(frame_corpo, command = lambda: entrada('5'), text='5', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=70, y=120)

b13 = Button(frame_corpo, command = lambda: entrada('6'), text='6', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=140, y=120 )

b14 = Button(frame_corpo, command = lambda: entrada('**2'), text='x²', width=5, height=2, bg=cor4, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=210, y=120)

b15 = Button(frame_corpo, command = lambda: entrada('+'), text='+', width=5, height=2, bg=cor4,fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=280, y=120)

b16 = Button(frame_corpo, command = lambda: entrada('1'), text='1', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=180)

b17 = Button(frame_corpo, command = lambda: entrada('2'), text='2', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=70, y=180)

b18 = Button(frame_corpo, command = lambda: entrada('3'), text='3', width=5, height=2, bg=cor7, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=140, y=180)

b19 = Button(frame_corpo, command = lambda: entrada('/100'), text='%', width=5, height=2, bg=cor4,fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b19.place(x=0, y=235)

b20 = Button(frame_corpo, command = lambda: entrada('0'), text='0', width=5, height=2, bg=cor7,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b20.place(x=70, y=235)

b21 = Button(frame_corpo, command = lambda: entrada('.'), text=',', width=5, height=2, bg=cor7,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b21.place(x=140, y=235)

b22 = Button(frame_corpo, command = lambda: entrada('-'), text='-', width=5, height=2, bg=cor4, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b22.place(x=210, y=180)

b23 = Button(frame_corpo, command = lambda: entrada('*'), text='x', width=5, height=2, bg=cor4,fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b23.place(x=210, y=235)

b24 = Button(frame_corpo, text='=', width=5, height=5, bg=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b24.place(x=280, y=180)


janela.mainloop()
