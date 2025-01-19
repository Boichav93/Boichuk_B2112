from tkinter import *
from tkinter import messagebox
from random import *

#Функція перевірки кінця гри
def isEnd():
    global field
    for i in range(15):
        if field[i]["text"] != str(i+1):
            return
    messagebox.showinfo("Congratulation","You won")
    exit(0)

#Функція пошуку пустої клітинки
def findEmptyCell():
    global field
    for i in range(16):
        if field[i]["text"] == "":
            return i

#Функція натискання на кнопки
def KeyPress(e):
    pos = findEmptyCell()
    if e.keycode == 38:#Up == 38
        if pos < 12:
            field[pos]["text"],field[pos+4]["text"] = field[pos+4]["text"],field[pos]["text"]
    if e.keycode == 37: #left = 37
        if (pos +1) % 4 !=0:
            field[pos]["text"], field[pos+1]["text"] = field[pos+1]["text"], field[pos]["text"]
    if e.keycode == 40: #down = 40
        if pos>3:
            field[pos]["text"], field[pos-4]["text"] = field[pos-4]["text"], field[pos]["text"]
    if e.keycode == 39:  # right = 39
        if pos % 4 != 4:
            field[pos]["text"], field[pos-1]["text"] = field[pos-1]["text"], field[pos]["text"]

#Функція створення поля

def setFiled():
    n=0
    for i in range(4):
        for j in range(4):
            field.append(Label(form, width=6,height=3, font="Arial 20 bold", borderwidth=1, relief="solid"))
            field[n].grid(row = i, column = j)
            n +=1
    k = 1
    while k < 16:
        a = randint(0,15)
        if(field[a]["text"] == ""):
            field[a]["text"] = str(k)
            k += 1


form = Tk()
form.title("Game")
form.resizable(False,False)
field = []
setFiled()
form.bind("<Key>", KeyPress)
form.mainloop()