from tkinter import *
root = Tk()

dalee = Button(root, text = 'Далее').place(x=270, y=270, height=50)
textfield = Entry()
textfield.place(x=235, y=200, height=50)
root.geometry("600x400")
root.title("Брокер ДБО")
writeText = Label(root, text = "Вопрос о сравнении критериев: ").place(x=200,y=100)
label1 = Label(root, text = "На сколько  + crit_list[temp_new] + важнее чем  + crit_list[crit_ask]) ").place(x=200,y=150)
root.mainloop()