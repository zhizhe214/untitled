from tkinter import *
w=Tk()
w.title('Entry练习')
w.geometry('1000x500')
w.wm_minsize(width=100,height=100)

def insert_point_event():
    var=e.get()
    t.insert('insert',var)

def indert_end_event():
    var=e.get()
    t.insert('end',var)

# 导入图片
ima=PhotoImage(file=r'E:\Peak\Desktop\timg.gif')

e=Entry(w,show='*')
e.pack()

b1=Button(w,text='insert point',width=ima.width(),height=ima.height(),
       command=insert_point_event,activebackground='red',image=ima)
b1.pack()
b2=Button(w,text='insert end',command=indert_end_event)
b2.pack()

t=Text(w,height=2)
t.pack()
help(print)
w.mainloop()