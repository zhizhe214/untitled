from tkinter import *
import tkinter.messagebox
import pickle
w=Tk()
w.geometry('1000x500')
w.title('登录界面')
# 登录和注册按钮需要用到的事件
def command_Ligin():
    # 这两行代码就是获取用户输入的`usr_name`和`usr_pwd`
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    ##这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    ##中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        ##这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        ##的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    # 这一部分就是将用户输入的用户名和密码获取到，和我们保存在usr_file中的数据对比。针对正确的密码和错误的密码分别对待.
    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗`how are you?`加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='欢迎登陆', message='How Are You? ' + usr_name)
        ##如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tkinter.messagebox.showerror(message='密码错误，请重试。')
    # 如果发现用户名不存在
    else:
        is_sign_up = tkinter.messagebox.askyesno('你还没有账号，现在注册码？')
        # 提示需不需要注册新用户
        if is_sign_up:
            command_Sign_Up()
    print('登录')

def command_Sign_Up():
    print('注册')
    pass
# 加载图片
img=PhotoImage(file=r'C:\Users\zhizh\PycharmProjects\untitled\welcome.gif')
l=Label(w,text=r'图片',image=img)
l.pack()

# userName Password
l_userName=Label(w,text='UserName').place(x=400,y=150)
l_passWord=Label(w,text='PassWord').place(x=400,y=190)
# l_userName.pack(side=LEFT)
# l_userName.pack()
# l_passWord.pack()
# 输入框
var_usr_name = StringVar()  #定义变量
var_usr_name.set('example@python.com')  #变量赋值'example@python.com'
#创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
e_userName=Entry(w,bg='#b2d235',fg='red',textvariable=var_usr_name).place(x=500,y=150)
#
var_usr_pwd=StringVar()
#`show`这个参数将输入的密码变为`***`的形式
e_passWord=Entry(w,bg='#b2d235',show='*',fg='red',textvariable=var_usr_pwd).place(x=500,y=190)
# e_userName.pack()
# e_passWord.pack()
# 按钮
b_Login=Button(w,text='Login',command=command_Ligin)
b_Login.place(x='500',y='230')
b_Sign=Button(w,text='Sign up',command=command_Sign_Up)
b_Sign.place(x='550',y='230')






w.mainloop()