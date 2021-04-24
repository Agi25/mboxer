#!/usr/bin/env python3
import socket
import os
import sys
import signal
import re
import hashlib

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',9999))
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
s.listen(5)

while True:
    connected_socket,address=s.accept()
    pid_chld=os.fork()
    if WRITE:
    if pid_chld==0:
        s.close()
        f=connected_socket.makefile(mode='rw',encoding='utf-8')
        f.write(f'Mailbox\n')
        f.flush()
        f.readline()
        n=0
        while True:
            request=f.readline().decode('ASCII')
            if not request:
                break
            print(request)
            m=re.match('([^ ]*)\n',request)
            if m:
                status=(100,'OK')
                content_reply=f'{n}\n'
                try:
                    n=int(m.group(1))
                except ValueError:
                     status=(200,'Bad request')
            elif request=='SUMA\n':
                status=(100,'OK')
                content_reply=''
            else:
                status=(203,'No such mailbox')
                content_reply=''
            f.write(f'Content-length:{status}\n')
            f.write('\n')
            f.flush()
        sys.exit(0)
    else:
        connected_socket.close()
        
