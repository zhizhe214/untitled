from tkinter import *
root_window=Tk()

def printRect(enent):
    print("rectangle - [左键]事件")
def printRect2(event):
    print("rectangle - [右键]事件")
def printLine(event):
    print('Line 事件')

canvas=Canvas(root_window,bg='#c77eb5')         # 创建canvas,设置其背景色为 #c77eb5
rt1=canvas.create_rectangle\
    (
    10,10,110,110,
    width=8, tags='r1'
    )
canvas.tag_bind('r1','<Button-1>',printRect)    # 绑定 item 与 鼠标左键事件
canvas.tag_bind('r1','<Button-3>',printRect2)   # 绑定 item 与 鼠标右键事件
# 创建一个 line ,并将其 tags 设置为‘r2’
canvas.create_line(180,70,280,70,width=10,tags="r2")
canvas.tag_bind('r2','<Button-1>',printLine)        # 绑定 item 与 鼠标左键事件
canvas.pack()

root_window.mainloop()