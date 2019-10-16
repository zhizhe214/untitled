import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time
# 发信方的信息：发信邮箱、邮箱授权码 / 密码
from_address = '1119663128@qq.com'
password = 'lkodcehywdkfjgjj'

# 收信方邮箱
#to_address = 'zhizhe214@163.com'
to_address=[]
while True:
    a=input('请输入收件人邮箱地址：')
    to_address.append(a)
    b=input('是否继续输入：“n”退出，任意键继续。')
    if b=="n":
        break
print(to_address)

# 发信服务器
smtp_server = 'smtp.qq.com'

# 开启发信服务，这里使用的是加密协议
server = smtplib.SMTP_SSL()
server.connect(smtp_server, 465)

# 邮件内容
bodyText = '''
    亲爱的学员，你好！
我是高峰，能遇见你很开心。
希望学习Python对你不是一件困难的事情！

   人生苦短，我用Python'''
msg = MIMEText(bodyText, 'plain', 'utf-8')
# 头信息
msg['From'] = Header('Python自动群发邮件  By 高峰')
msg['To'] = Header(",".join(to_address))
msg['Subject'] = Header('Python发送邮件测试')

# 登录发信邮箱
server.login(from_address, password)
# 发送邮件
for i in range(100):
    server.sendmail(from_address, to_address, msg.as_string())
    time.sleep(10)
# 关闭服务器
server.quit()
print("邮件发送完成")

















