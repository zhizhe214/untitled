from tkinter import *
root=Tk()
root.geometry('500x200')
# 创建两个 Frame 作为容器
frame_1=Frame(root,bg='red',width=400,height=100)
frame_2=Frame(root,bg='blue',width=300,height=40)

# 再在 frame_1 中创建一个 frame_3
frame_3=Frame(frame_1,bg='yellow',width=150,height=50)
frame_3.place(relx=0.4,rely=0.5,anchor=E)
# # 再创建一个 Label ,它的master为 frame_1
label_1=Label(frame_1,text='label_1',bg='green')
label_1.place(in_=frame_1,relx=0.5,rely=0.5,anchor=CENTER)
#  # 再创建一个 button_1,它的master为frame_1
button_1=Button(frame_1,text='button_1')
button_1.place(in_=frame_3,x=15,rely=0.5,anchor=W)


frame_1.pack()
frame_2.pack()
# frame_3.pack()
root.mainloop()