#!/bin/back
#!/usr/bin/emu python3

import socket as so
d = input("Domain: ") 

S = so.socket(so.AF_INET, so.SOCK_STREAM)
S.connect((d, 80))
S.send(b"GET / http1.1\r\nhost: "+bytes(d,"UTF8")+b"\r\nConnection: close\r\n\r\n")
reply=S.recv(10000)
S.shutdown(so.SHUT_RDWR)
S.close()
print(repr(reply))

