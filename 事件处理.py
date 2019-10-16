import tkinter
import tkinter.messagebox

w = tkinter.Tk()
w.title('事件处理练习')
w.geometry('400x200')
w.resizable(False,False)

def callback():
    # 提示消息框
    # tkinter.messagebox.showinfo('提示','事件处理')
    # 消息警告框
    # tkinter.messagebox.showwarning('警告框', '想死是吧？？？')
    # 错误消息框
    # tkinter.messagebox.showerror('错误消息框','错误啦')
    ask=tkinter.messagebox.askokcancel('提示','你忍心离我而去吗？')
    print(ask)     #点击 确定返回 Ture; 取消返回 False


btn = tkinter.Button(text='点我呀', bg='yellow', command=callback)
btn.pack()
w.mainloop()
