import tkinter as tk
import tkinter.font
num=0
def Btn_1():
    global num
    num+=1
    print("我发誓: "+str(num))
w=tk.Tk()
w.title("事件绑定")
w.geometry('1000x500')
# 声明 [可以共用的] 字体变量
my_font2=tk.font.Font(family='楷体',size=28,slant='italic',underline=1,overstrike=1)

b=tk.Button(w,text="点我",bg='green',fg='white',font=('微软雅黑',18,'bold italic'),width='10',command=Btn_1)
b.pack(side=tk.TOP)
b2=tk.Button(w,text="点我",bg='green',fg='yellow',font=my_font2,width='10',command=Btn_1)
b2.pack(side=tk.TOP)

l=tk.Label(w,text='水电费',bg='blue',fg='red',font=('楷体','22','italic'))
l.pack(side=tk.BOTTOM)
l2=tk.Label(w,text='水电费',bg='#f3704b',fg='blue',font=my_font2)
l2.pack(side=tk.BOTTOM)

e=tk.Entry(w,show='+')
e.pack()
w.mainloop()