from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" #black
cor2 = "#feffff" #white
cor3 = "#38576b" #blue
cor4 = "#ECEFF1" #gray
cor5 = "#FFAB40" #orange

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x300")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# funções

todoValores = ""
valorTexto = StringVar()
 
def entrarValores(event):
    global todoValores
    todoValores = todoValores + str(event)

    valorTexto.set(todoValores)

def calc():
    global todoValores
    try:
        res = eval(todoValores)
        valorTexto.set(res)
        todoValores = str(res)
    except ZeroDivisionError:
        valorTexto.set("Cannot divide by 0")
        todoValores = " "

def limpar():
    global todoValores
    valorTexto.set("")
    todoValores = ""


# criando label


app_label = Label(frame_tela, textvariable=valorTexto, width=15, height=2, bg=cor1, fg=cor2, font=('Ivy 18 bold'), padx=7, relief=FLAT, anchor="e", justify=RIGHT)
app_label.place(x=0, y=0)


# botões
# row 1
b11 = Button(frame_corpo, command=limpar, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=0, y=0)

b12 = Button(frame_corpo, command=lambda:entrarValores("%"),text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=118, y=0)

b13 = Button(frame_corpo,  command=lambda:entrarValores("/"),text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=177, y=0)

# row 2
b21 = Button(frame_corpo,  command=lambda:entrarValores("7"),text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b21.place(x=0, y=50)

b22 = Button(frame_corpo,  command=lambda:entrarValores("8"),text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b22.place(x=59, y=50)

b23 = Button(frame_corpo,  command=lambda:entrarValores("9"),text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b23.place(x=118, y=50)

b24 = Button(frame_corpo,  command=lambda:entrarValores("*"),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b24.place(x=177, y=50)

#row 3
b31 = Button(frame_corpo,  command=lambda:entrarValores("4"),text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b31.place(x=0, y=100)

b32 = Button(frame_corpo,  command=lambda:entrarValores("5"),text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b32.place(x=59, y=100)

b33 = Button(frame_corpo,  command=lambda:entrarValores("6"),text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b33.place(x=118, y=100)

b34 = Button(frame_corpo,  command=lambda:entrarValores("-"),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b34.place(x=177, y=100)

#row 4
b41 = Button(frame_corpo,  command=lambda:entrarValores("1"),text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b41.place(x=0, y=150)

b42 = Button(frame_corpo,  command=lambda:entrarValores("2"),text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b42.place(x=59, y=150)

b43 = Button(frame_corpo,  command=lambda:entrarValores("3"),text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b43.place(x=118, y=150)

b44 = Button(frame_corpo,  command=lambda:entrarValores("+"),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b44.place(x=177, y=150)

#row 5
b51 = Button(frame_corpo,  command=lambda:entrarValores("0"),text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b51.place(x=0, y=200)

b52 = Button(frame_corpo,  command=lambda:entrarValores("."),text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b52.place(x=118, y=200)

b53 = Button(frame_corpo,  command=calc, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b53.place(x=177, y=200)

janela.mainloop()
 