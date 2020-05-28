'''
from tkinter import *
root = Tk()

fizl = Button(root, text = 'Физические лица').place(x=100, y=150, height=100)
yurl = Button(root, text = 'Юридические лица').place(x=400, y=150, height=100)
root.geometry("600x400")
root.title("Брокер ДБО")
root.mainloop()
import tkinter

root = tkinter.Tk()
lab = tkinter.Label(root, text="привет")
lab.grid(row=1, column=1)
lab['text'] = 'абракадабра'
lab['text'] = 'абракадабра'
ainloop()
#!/usr/bin/env python3
from tkinter import Tk, Button, Label

NBUTTONS = 3
root = Tk()
label = Label(text="no button pressed")
label.grid(row=1, columnspan=NBUTTONS)
for i in range(NBUTTONS):
    t = f"button {i+1}"
    b = Button(text=t, command=lambda t=t: label.configure(text=t))
    b.grid(row=0, column=i)
root.mainloop()
'''
import pandas as pd
import numpy as np
from tkinter import *


dataset = pd.read_csv("dbo.csv", sep=';', encoding='cp1251')
data = dataset
my_columns = data['Банки']
del data['Банки']
print(data)

'''Main X'''
'''asck=0
asc=0
while asck == 0:
    try:
        asc = int(input("Вы выступаете в роли физического или юридического лица: \n"
                        "1.Юридическое лицо \n "
                        "2.Физическое лицо\n"))
        if asc > 2 or asc < 1:
            print("Числа от 1 до 2")
            continue
        else:


    root = Tk()
    dalee = Button(root, text='Далее').place(x=270, y=270, height=50)
    textfield = Entry().place(x=235, y=200, height=50)
    root.geometry("600x400")
    root.title("Брокер ДБО")
    writeText = Label(root, text="Вопрос о сравнении критериев: ").place(x=200, y=100)
    label1 = Label(root, text="На сколько  + crit_list[temp_new] + важнее чем  + crit_list[crit_ask]) ").place(x=200, y=150)
    root.mainloop()'''
clicks=0
clickf=0
def click_button():
    global clicks
    clicks += 1
    first.destroy()
def click_buttonfiz():
    global clickf
    clickf += 1
    first.destroy()

first = Tk()
fizl = Button(first, text='Физические лица').place(x=100, y=150, height=100)
yurl = Button(first, text='Юридические лица', command=click_button)
yurl.place(x=400, y=150, height=100)
first.geometry("600x400")
first.title("Брокер ДБО")
#first.destroy()
first.mainloop()
if clicks == 1:

                data.drop(data.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)
                '''
               # first.destroy()
                root = Tk()
                dalee = Button(root, text='Далее').place(x=270, y=270, height=50)
                textfield = Entry().place(x=235, y=200, height=50)
                root.geometry("600x400")
                root.title("Брокер ДБО")
                writeText = Label(root, text="Вопрос о сравнении критериев: ").place(x=200, y=100)
                label1 = Label(root, text="На сколько  + crit_list[temp_new] + важнее чем  + crit_list[crit_ask]) ").place(x=200, y=150)
                root.mainloop()'''
else:
                asc=2
                data.drop(data.columns[[13, 14, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
                '''
                root = Tk()
                dalee = Button(root, text='Далее').place(x=270, y=270, height=50)
                textfield = Entry().place(x=235, y=200, height=50)
                root.geometry("600x400")
                root.title("Брокер ДБО")
                writeText = Label(root, text="Вопрос о сравнении критериев: ").place(x=200, y=100)
                label1 = Label(root,
                               text="На сколько  + crit_list[temp_new] + важнее чем  + crit_list[crit_ask]) ").place(
                    x=200, y=150)
                root.mainloop()'''

root = Tk()
mod=StringVar()
clickd=0
crit_list = list(data)
temp_new = 0
crit_ask = 1
def click_buttond():
    global clickd
    global mod
    global crit_list
    global temp_new
    global crit_ask
    mod = textfield.get()
    label1.config(text=f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
                f"Введите множители для критериев по важности. 1-неважно. 9-важно:")
    clickd += 1


dalee = Button(root, text='Далее', command=click_buttond)
dalee.place(x=270, y=270, height=50)
textfield = Entry()
label1 = Label(root, text="no button pressed")
label1.place(x=200, y=150)
#label1.pack()
textfield.place(x=235, y=200, height=50)
root.geometry("600x400")
root.title("Брокер ДБО")
writeText = Label(root, text="Вопрос о сравнении критериев: ").place(x=200, y=100)

root.mainloop()

asck = 1


main_x = []

input_new = []

mult = []
square = []
W = []



lensM = len(data.columns)
rowsM = len(data.index)
print(rowsM)
new = np.zeros((lensM, lensM))
np.fill_diagonal(new, 1)
counter = int(((new == 0).sum())/2)

critPlus = 1

'''t = f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
    f"Введите множители для критериев по важности. 1-неважно. 9-важно:"'''
while temp_new < counter:
    while crit_ask < lensM:

       # mod2 = int(mod)
        if clickd == 0:

            t = f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
                f"Введите множители для критериев по важности. 1-неважно. 9-важно:"

            label1['text'] = t
            #label1['text'] = f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
               # f"Введите множители для критериев по важности. 1-неважно. 9-важно:"

        else:
            label1['text'] = f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
                f"Введите множители для критериев по важности. 1-неважно. 9-важно:"
            #dalee = Button(root, text='Далее', command=click_buttond)
          #dalee = Button(command=lambda t=t: label1.configure(text=f"На сколько {crit_list[temp_new]} важнее чем {crit_list[crit_ask]}" \
            #    f"Введите множители для критериев по важности. 1-неважно. 9-важно:"))
         #textfield = Entry(textvariable=mod)


        if mod > 9 or mod< 1:
             print("Числа от 1 до 9")
             continue
        else:
             input_new.append(int(mod))




        crit_ask += 1
    critPlus += 1
    crit_ask = 0
    crit_ask += critPlus
    temp_new += 1

root.mainloop()
inds = np.triu_indices_from(new, k=1)
new[inds] = input_new
my_new_list = [1 / i for i in input_new]
new[(inds[1], inds[0])] = my_new_list
print(new)