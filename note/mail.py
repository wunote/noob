#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr,parseaddr

from_addr = 'y12.123l@163.com'
password = 'wu407894311'
to_addr = '407894311@qq.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

try:
    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode() 

    server=smtplib.SMTP(smtp_server,25)
    server.login(from_addr, password)
    server.sendmail(from_addr,[to_addr,],msg.as_string())
    server.quit()
    print('邮件发送成功！')
except Exception, e:
    print(str(e))
 
