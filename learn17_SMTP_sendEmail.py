# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:33:42 2018

@author: Waves
"""

#SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。 


#首先我们先构造纯文本的邮件：（网易邮箱 —>qq邮箱）
#参数1：邮件正文（hello,world） 
#参数2：MIME的subtype,传入‘plain’，最终的MIME就是’text/plain’ 
#参数3：代表编码
from email import encoders
from email.header import Header 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

#用来格式化邮件地址  
def _format_addr(s):
    name, addr = parseaddr(s)#这个函数会解析出姓名和邮箱地址
    return formataddr((Header(name, 'utf-8').encode(),addr))

#输入Email地址和口令
from_addr = input('From: ')
from_addr = 'waveschj@163.com'
#这里的密码一定是授权码，163邮箱原始密码不行。授权码在邮箱里设置
password = 'next***'
password = input('Password: ')
# 输入SMTP服务器地址:这里我们用smtp.163.com
smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'
# 输入收件人地址:
to_addr = input('To: ')
to_addr = 'waveschj@qq.com'


############发送文字邮件
#msg = MIMEText('hello world', 'plain', 'utf-8')

############发送HTML邮件 
"""
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="https://blog.csdn.net/Waves___">csdn</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
"""

############发送带附件的邮件
#带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
#所以，可以构造一个MIMEMultipart对象代表邮件本身，
#然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
# 邮件对象: 
msg = MIMEMultipart()
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8')) 
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)





#设置发件人，收件人姓名和邮件主题
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'朋友 <%s>' % to_addr)
msg['Subject'] = Header(u'测试邮件……', 'utf-8').encode()

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)#登录服务器
#发送邮件，这里第二个参数是个列表，可以有多个收件人
#邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

 
