#!/usr/bin/env python3
import socket
import os
import sys
import signal
import hashlib

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',9999))
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
s.listen(5)

while True:
    connected_socket,address=s.accept()
    print(f'spojenie z {address}')
    pid_chld=os.fork()
    if pid_chld==0:
        s.close()
        f=connected_socket.makefile('rwb')
        while True:
            stat_num=100
            stat_com="OK"
            odpovedh=""
            odpovedo=""
            metoda=f.readline().decode("ASCII")
            metoda=metoda.strip()
            
            header=f.readline().decode("ASCII")
            while header!="\n":
                if header.find(":"):
                    header=header.split(":")
                    header[0]=h
                    header[1]=o
                    if header.find("/"):
                        header=header.split("/")
                        header[0]=h
                        header[1]=o
                    else:
                        return (h,o)
            if metoda=="WRITE":
                try:
                    rep=f.read()
                    m=hashlib.md5(rep)
                    f.write('Content-length:{len(m)}').encode("ASCII")
                    f.write('\n').encode("ASCII")
                except KeyError:
                    stat_num,stat_com=(200,"Bad request")
                except FileNotFoundError:
                    stat_num,stat_com=(203,"No such mailbox")
            elif metoda="READ"
                try:
                    odpovedo=f.read().decode("ASCII")
                    odpovedh=f.write('Content-length:{len(odpovedo)'}.encode("ASCII")
                    f.write('\n').encode("ASCII")
                except KeyError:
                    stat_num,stat_com=(200,"Bad request")
                except FileNotFoundError:
                    stat_num,stat_com=(201,"No such message")
                except OSError:
                    stat_num,stat_com=(202,"Read error")
            elif metoda=="LS":
                try:
                    odpovedo=f.read().decode("ASCII")
                    odpovedh=f.write('Number-of-messages:{len(odpovedo)}').encode("ASCII")
                    f.write('\n').encode("ASCII")
                except KeyError:
                    stat_num,stat_com=(200,"Bad request")
                except FileNotFoundError:
                    stat_num,stat_com=(203,"No such mailbox")
        f.write(f'(stat_num) (stat_com)'.encode("ASCII")
        f.write('\n').encode("ASCII")
        f.write(odpovedh).encode("ASCII")
        f.write('\n').encode("ASCII")
        f.write(odpovedo).encode("ASCII")
        f.write('\n').encode("ASCII")
        f.flush()
        print(f'{address} uzavrel spojenie')
        sys.exit(0)
    else:
        connected_socket.close()
