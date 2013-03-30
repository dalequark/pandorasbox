#!/usr/bin/env python 

import socket
import threading
from Tkinter import *

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)


class Imager(threading.Thread):

    master = Tk()
    w = Canvas(master, width=200, height=100)

    def run(self):

      self.w.pack()

      self.w.create_line(0, 0, 200, 100)
      self.w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

      self.w.create_text(100,50,text="Dale", tags="test")

      self.master.mainloop()

    def changename(self, newname):
      self.w.delete("test")
      self.w.create_text(100,50,text=newname, tags="test")
		

image = Imager()
image.start()

while True:
    client, address = s.accept()
    data = client.recv(size)
    buffer = data
    while len(buffer) > 0:
        buffer = client.recv(size)
        data += buffer
    if len(data) > 0:
        image.changename(data)
        client.send("Data received: " + data)
    client.close() 



#this is the gui part of the program
'''
master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_text(100,50,text=name)

master.mainloop()
'''
