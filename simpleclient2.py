#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import fileinput

host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
for line in fileinput.input():
   print line
   totalsent = 0
   while totalsent < len(line):
      totalsent += s.send(line[totalsent:])
s.close()
print 'sent'
