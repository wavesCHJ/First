# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:39:21 2018

@author: c84109001
"""

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据
    s.sendto(data, ('127.0.0.1', 8999))
    time.sleep(1)
    #接收数据
    print(s.recv(1024).decode('utf-8'))
s.close
