# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:10:09 2018

@author: c84109001
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1', 8999))
#接受欢迎信息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close
