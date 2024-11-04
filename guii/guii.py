from tkinter import *
import tkinter.ttk as ttk


#----------------------내용----------------------
lines1 = open("1번째.txt", 'r', encoding='UTF-8').readlines()
lines11 = []
for a in lines1:
    lines11.append(a.strip())


lines2 = open("2번째.txt", 'r', encoding='UTF-8').readlines()
lines22 = []
for b in lines2:
    lines22.append(b.strip())


lines3 = open("3번째.txt", 'r', encoding='UTF-8').readlines()
lines33 = []
for c in lines3:
    lines33.append(c.strip())

#--------------------기능-----------------------

def output():
   text.delete("1.0", END)
   text.insert(END, combobox1.get() +" "+ combobox2.get() +" "+ combobox3.get())

def erase():
    text.delete("1.0", END)


#----------------ui--------------------
win = Tk()
win.title('무언가 대충 생기부 프로그램')
win.geometry("1400x300")
#목록

lab1 = Label(win, text='첫번째 쏼라쏼라')
lab1.grid(row= 0, column= 1)

lab1 = Label(win, text='두번째 쏼라쏼라')
lab1.grid(row= 0, column= 2)

lab1 = Label(win, text='세번째 쏼라쏼라')
lab1.grid(row= 0, column= 3)

combobox1 = ttk.Combobox(win, height= 8, width= 60, values= lines11, state="readonly")
combobox1.grid(row=1, column=1)
combobox1.set('1번째')

combobox2 = ttk.Combobox(win, height= 8, width= 60, values= lines22, state="readonly")
combobox2.grid(row=1, column=2)
combobox2.set('2번째')

combobox3 = ttk.Combobox(win, height= 8, width= 60, values= lines33, state="readonly")
combobox3.grid(row=1, column=3)
combobox3.set('3번째')

#출력

text = Text(win, width= 60, height=4)
text.grid(row=2, column=2, pady= 20)

btn1 = Button(win, text='만들기', command= output)
btn1.grid(row= 3, column= 2)

btn3 = Button(win, text='지우기', command= erase)
btn3.grid(row= 5, column= 2)

lab = Label(win, text='뀨')
lab.grid(row= 6, column= 2)

win.mainloop()















