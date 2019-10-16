from tkinter import *
root=Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
ww=900
wh=500
x=(screen_width-ww)/2
y=(screen_height-wh)/2
root.geometry('%dx%d+%d+%d'%(ww,wh,x,y))

# root.geometry('600x400+500+500')
lable_1=Label(root,text='label_1',bg='pink')
label_2=Label(root,text='label_2',bg='yellow')
label_3=Label(root,text='label_3',bg='red')
label_4=Label(root,text='label_4',bg='green')

lable_1.grid(row=0,column=0)
label_2.grid(row=0,column=1)
label_3.grid(row=1,column=1)
label_4.grid(row=2,column=1)

print('屏幕宽度：%d，\n屏幕高度：%d' %(root.winfo_screenwidth(),root.winfo_screenheight()))
root.mainloop()