from tkinter import *
root = Tk()

glavn = Button(root, text = 'На главную').place(x=270, y=270, height=50)
root.geometry("600x400")
root.title("Брокер ДБО")
writeText = Label(root, text = "Система предлагает Вам воспользоваться услугами банка: ").place(x=200,y=100)
label1 = Label(root, text = "вывод банка ").place(x=200,y=150)
root.mainloop()