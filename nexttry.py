import pandas as pd
import numpy as np
import tkinter as tk
import tkinter as ttk


dataset = pd.read_csv("dbo.csv", sep=';', encoding='cp1251')
data = dataset
my_columns = data['Банки']
del data['Банки']
print(data)
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
first = tk.Tk()
fizl = tk.Button(first, text='Физические лица', command=click_buttonfiz).place(x=100, y=150, height=100)
yurl = tk.Button(first, text='Юридические лица', command=click_button)
yurl.place(x=400, y=150, height=100)
first.geometry("600x400")
first.title("Брокер ДБО")
first.mainloop()
asc=0

if clicks == 1:
    data.drop(data.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)
    asc = 1
else:
    data.drop(data.columns[[13, 14, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
    asc = 2

main_x = []
input_new = []
mult = []
square = []
W = []
temp_new = 0
lensM = len(data.columns)
rowsM = len(data.index)
new = np.zeros((lensM, lensM))
np.fill_diagonal(new, 1)
counter = int(((new == 0).sum())/2)
crit_ask = 1
critPlus = 1
crit_list = list(data)
clickd=0


def click_buttond():
    global clickd
    global temp_new
    global crit_ask
    global critPlus
    global mod

    clickd = clickd+1
    print(clickd)
    if asc==1:
      if clickd > 36:
        second.destroy()
    else:
      if clickd>89:
          second.destroy()


    while temp_new < counter:
        while crit_ask < lensM:


            try:
                mod = textfield.get()
                if int(mod) > 9 or int(mod) < 1:
                    print("Числа от 1 до 9")
                    continue
                else:
                    input_new.append(int(mod))

            except ValueError:

                continue
            label1.config(text=f"На сколько {crit_list[temp_new]}  важнее чем {crit_list[crit_ask]}")
            crit_ask = crit_ask + 1


            second.mainloop()


        critPlus += 1
        crit_ask = 0
        crit_ask += critPlus
        temp_new += 1


        second.mainloop()






second= tk.Tk()
dalee = tk.Button(second, text='Далее', command=click_buttond)
dalee.place(x=270, y=270, height=50)
textfield = ttk.Entry()
textfield.place(x=235, y=200, height=50)
second.geometry("600x400")
second.title("Брокер ДБО")
writeText = tk.Label(second, text="Вопрос о сравнении критериев: ").place(x=200, y=100)
label1 = tk.Label(second, text=f"На сколько {crit_list[temp_new]}  важнее чем {crit_list[crit_ask]}")
label1.place(x=200, y=150)

second.mainloop()



inds = np.triu_indices_from(new, k=1)
new[inds] = input_new
my_new_list = [1 / i for i in input_new]
new[(inds[1], inds[0])] = my_new_list
print(new)

y = 0
mu = 1
temp_mu = 0
while temp_mu < lensM:
    while y < lensM:
        mu *= new[temp_mu][y]
        y += 1
    mult.append(mu)
    mu = 1
    y = 0
    temp_mu += 1

square = [i ** (1/len(mult)) for i in mult]
sum_sq = sum(square)

W = [(j / sum_sq) for j in square]
print("Sum " + str(W))

'''Categories'''

input_new_each = []
temp_new_each = 0
crit_ask_each = 1
#crit_ask_each = 0
critPlusCrit = 1

mult_each = []
square_each = []
p = []
if asc == 2:
    mn = 10
else:
    mn = 1000
for col in data:
    new_each = np.zeros((rowsM, rowsM))
    np.fill_diagonal(new_each, 1)
    counter = int(((rowsM * rowsM - rowsM) / 2))
    crit_list_each = list(data[col])
    while temp_new_each < counter:
        while crit_ask_each < rowsM:
            if (crit_list_each[temp_new_each]) == (crit_list_each[crit_ask_each]):
                input_new_each.append(1)
            elif col == "Безопасность" or col == "Безопасность.1" or col == "Открытие вклада" or \
                    col == "Оформление кредита" or col == "Оформление вкладов" or col == "Электронный кошелек":
                if (crit_list_each[temp_new_each]) == "Доступно" and crit_list_each[crit_ask_each] == "Не доступно":
                    input_new_each.append(9)
                elif (crit_list_each[temp_new_each]) == "Не доступно" and crit_list_each[crit_ask_each] == "Доступно":
                    input_new_each.append(2)
                elif ((crit_list_each[temp_new_each]) == "стандарт + 3d rescue, автооотключ сеанса" or
                      crit_list_each[temp_new_each] == "протокол ssl, 3d rescue, автооотключ сеанса" or
                      crit_list_each[temp_new_each] == "стандарт +  3d rescue") and \
                        crit_list_each[crit_ask_each] == "стандарт":
                    input_new_each.append(9)
                elif (crit_list_each[temp_new_each]) == "стандарт " and \
                        (crit_list_each[crit_ask_each] == "стандарт + 3d rescue, автооотключ сеанса"or
                      crit_list_each[crit_ask_each] == "протокол ssl, 3d rescue, автооотключ сеанса" or
                      crit_list_each[crit_ask_each] == "стандарт +  3d rescue"):
                    input_new_each.append(2)
                elif ((crit_list_each[temp_new_each]) == "стандарт + 3d rescue, автооотключ сеанса" or
                      crit_list_each[temp_new_each] == "протокол ssl, 3d rescue, автооотключ сеанса" or
                      crit_list_each[temp_new_each] == "стандарт +  3d rescue") and \
                        (crit_list_each[crit_ask_each] == "стандарт + 3d rescue, автооотключ сеанса"or
                      crit_list_each[crit_ask_each] == "протокол ssl, 3d rescue, автооотключ сеанса" or
                      crit_list_each[crit_ask_each] == "стандарт +  3d rescue"):
                    input_new_each.append(1)
                elif ((crit_list_each[temp_new_each]) == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., автооотключ сеанса, аутент. уровня транзакций, СКЗИ и ЭПЦ" or
                      crit_list_each[temp_new_each] == "антивирусное ПО, протокол ssl, аппаратная аутентифик., автооотключ сеанса, аутент. уровня транзакций, СКЗИ и ЭПЦ" or
                      crit_list_each[temp_new_each] == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., СКЗИ и ЭПЦ" or
                        crit_list_each[temp_new_each] == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., аутент. уровня транзакций, СКЗИ и ЭПЦ")and \
                        (crit_list_each[crit_ask_each] == "антивирусное ПО, протокол ssl, проверка ip, СКЗИ и ЭПЦ" or
                         crit_list_each[crit_ask_each] == " проверка ip, автооотключ сеанса"):
                    input_new_each.append(9)
                elif ((crit_list_each[crit_ask_each]) == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., автооотключ сеанса, аутент. уровня транзакций, СКЗИ и ЭПЦ" or
                      crit_list_each[crit_ask_each] == "антивирусное ПО, протокол ssl, аппаратная аутентифик., автооотключ сеанса, аутент. уровня транзакций, СКЗИ и ЭПЦ" or
                      crit_list_each[crit_ask_each] == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., СКЗИ и ЭПЦ" or
                        crit_list_each[crit_ask_each] == "антивирусное ПО, протокол ssl, проверка ip, аппаратная аутентифик., аутент. уровня транзакций, СКЗИ и ЭПЦ")and \
                        (crit_list_each[temp_new_each] == "антивирусное ПО, протокол ssl, проверка ip, СКЗИ и ЭПЦ" or
                         crit_list_each[temp_new_each] == " проверка ip, автооотключ сеанса"):
                    input_new_each.append(2)
                else:
                    input_new_each.append(1)
            elif float(crit_list_each[temp_new_each]) == 1 and float(crit_list_each[crit_ask_each]) == 0:
                input_new_each.append(9)
            elif float(crit_list_each[temp_new_each]) == 0 and float(crit_list_each[crit_ask_each]) == 1:
                input_new_each.append(2)
            elif float(crit_list_each[temp_new_each]) < float(crit_list_each[crit_ask_each]):
                if float(crit_list_each[temp_new_each]) == 0:
                    input_new_each.append(9)
                elif float(crit_list_each[crit_ask_each])-float(crit_list_each[temp_new_each]) > mn:
                    input_new_each.append(8)
                elif float(crit_list_each[crit_ask_each])-float(crit_list_each[temp_new_each]) < mn:
                    input_new_each.append(6)
            elif float(crit_list_each[temp_new_each]) > float(crit_list_each[crit_ask_each]):
                if float(crit_list_each[crit_ask_each]) == 0:
                    input_new_each.append(2)
                elif float(crit_list_each[temp_new_each]) > float(crit_list_each[crit_ask_each]) > mn:
                    input_new_each.append(4)
                elif float(crit_list_each[temp_new_each]) > float(crit_list_each[crit_ask_each]) < mn:
                    input_new_each.append(3)
            else:
                input_new_each.append(1)

            crit_ask_each += 1
        critPlusCrit += 1
        crit_ask_each = 0
        crit_ask_each += critPlusCrit
        temp_new_each += 1
    re=0
    ri=0
    if len(input_new_each) != 153:
        re=153-len(input_new_each)
        while ri < re:
            input_new_each.append(5)
            ri += 1
    inds_each = np.triu_indices_from(new_each, k=1)
    new_each[inds_each] = input_new_each
    my_new_list = [("%.2f" % (1 / i)) for i in input_new_each]
    new_each[(inds_each[1], inds_each[0])] = my_new_list
    inds_each = 0
    input_new_each = []
    critPlusCrit = 1

    y_each = 0
    mu_each = 1
    temp_mu_each = 0
    while temp_mu_each < rowsM:
        while y_each < rowsM:
            mu_each *= new_each[temp_mu_each][y_each]
            y_each += 1
        mult_each.append(mu_each)
        mu_each = 1
        y_each = 0
        temp_mu_each += 1

    square_each = [(i ** (1 / len(mult_each))) for i in mult_each]
    sum_sq_each = sum(square_each)

    p = [(j / sum_sq_each) for j in square_each]
    print("Sum " + str(p))
    main_x.append(p)
    #crit_ask_each = 0
    crit_ask_each = 1
    temp_new_each = 0
    critPlusCrit = 1
    mult_each = []
    square_each = []
    p = []
matrix = np.array(main_x)
print(matrix)

'''Result'''
result = []
row_count = 0
col_count = 0
res_row = 0
res = 0
colM = len(matrix[0])
rowsesM = len(matrix)
while col_count < colM:
    while row_count < rowsesM:
        res += (matrix[row_count][col_count] * W[row_count])
        row_count += 1
    result.append(res)
    res = 0
    col_count += 1
    row_count = 0
print(result)

dictionary = dict(zip(my_columns, result))
print(dictionary)
best = 0



dictionary=sorted(dictionary.items(), key=lambda para: para[1], reverse=True)

print(dictionary)
def click_buttonfinal():

          label2.config(text=dictionary[0])
          label3.config(text=dictionary[1])
          label4.config(text=dictionary[2])
          third.mainloop()


third = tk.Tk()
glavn = tk.Button(third, text = 'Показать банки', command = click_buttonfinal)
glavn.place(x=270, y=270, height=50)
third.geometry("600x400")
third.title("Брокер ДБО")
writeText = tk.Label(third, text = "Система предлагает Вам воспользоваться услугами банков: ").place(x=200,y=100)
label2 = tk.Label(third, text = "Интрига ))")
label2.place(x=200, y=150)
label3 = tk.Label(third, text = "Интрига ))")
label3.place(x=200, y=170)
label4 = tk.Label(third, text = "Интрига ))")
label4.place(x=200, y=190)
third.mainloop()

