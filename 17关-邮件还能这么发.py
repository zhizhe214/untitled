import smtplib
from email.header import Header
from email.mime.text import MIMEText

# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
'''
with SMTP_SSL(host="smtp.163.com") as smtp :
    smtp.login(user='zhizhe214@163.com',password='zhizhuo214')

    msg = MIMEText("这是来自Python3的一封测试邮件",_charset="utf8")
    msg["Subject"] = "测试邮件"
    msg["from"] = 'zhizhe214@163.com'
    msg["to"] = 'zhizhe214@163.com'

    smtp.sendmail(from_addr="zhizhe214@163.com",to_addrs="zhizhe214@163.com", msg=msg.as_string())
'''

# 发信方的信息：发信邮箱、邮箱授权码 / 密码
from_address = '1119663128@qq.com'
password = 'lkodcehywdkfjgjj'
# password='911dangbo214'

# 收信方邮箱
#to_address = 'zhizhe214@163.com'
to_address=['zhizhe214@163.com','zhizhe214@126.com']

# 发信服务器
smtp_server = 'smtp.qq.com'

# 开启发信服务，这里使用的是加密协议
server = smtplib.SMTP_SSL()
server.connect(smtp_server, 465)

# 邮件内容
bodyText = '''
    亲爱的学员，你好！
我是吴枫老师，能遇见你很开心。
希望学习Python对你不是一件困难的事情！

   人生苦短，我用Python'''
msg = MIMEText(bodyText, 'plain', 'utf-8')
# 头信息
msg['From'] = Header('我是邮件主题')
msg['To'] = Header(",".join(to_address))
msg['Subject'] = Header('Python发送邮件测试')

# 登录发信邮箱
server.login(from_address, password)
# 发送邮件
server.sendmail(from_address, to_address, msg.as_string())

# 关闭服务器
server.quit()


















