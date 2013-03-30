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

def changename(newname):
  w.delete("test")
  w.create_text(100,50,text=newname, tags="test")

class Poller(threading.Thread):

  def run(self):

    while(True):

      client, address = s.accept()
      data = client.recv(size)
      buffer = data
      while len(buffer) > 0:
          buffer = client.recv(size)
          data += buffer
      if len(data) > 0:
          changename(data)
          client.send("Data received: " + data)
      client.close() 
		

poller = Poller()
poller.start()

master = Tk()
w = Canvas(master, width=200, height=100)
w.create_text(100,50,text="Dale", tags="test")
w.pack()
master.mainloop()

    



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
