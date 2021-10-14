from tkinter import *
from string import *

def process_shift(text = '', shift = 0):
    try:
        shift = int(txt2.get())
        text = str(txt1.get())
    except:
        return
    result = ''
    letters = ascii_lowercase + ' '
    for x in range(len(text)):
        tempshift = letters.find(text[x].lower()) + shift
        while tempshift < 0 or tempshift >= len(letters):
            if tempshift < 0: tempshift += len(letters)
            else: tempshift -= len(letters)
        result += letters[tempshift]
    resulttxt.delete(0, END)
    resulttxt.insert(0, result)

gui = Tk()
gui.geometry('250x90+800+400')
gui.resizable(width = False, height = False)

btn1 = Button(gui, text = 'Shift', width = 8, command = process_shift, bg = '#FF00FF', activebackground = '#00FF00')
btn1.place(x = 145, y = 29)

lbl1 = Label(gui, text = 'Text to shift:')
lbl1.place(x = 5, y = 5)
lbl2 = Label(gui, text = 'Shift factor:')
lbl2.place(x = 5, y = 32)
lbl3 = Label(gui, text = 'Shifted text:')
lbl3.place(x = 5, y = 59)

txt1 = Entry(gui, width = 25)
txt1.place(x = 80, y = 5)
txt2 = Entry(gui, width = 5)
txt2.place(x = 80, y = 32)

resulttxt = Entry(gui, width = 25)
resulttxt.place(x = 80, y = 59)

gui.mainloop()
