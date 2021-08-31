
import socket

from _thread import *
import threading

import tkinter as tk

conn_lock = threading.Lock()

host = "192.168.0.109"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("socket binded to port", port)

s.listen()

print("socket is listening")


def threaded(c):

    root.update()

    msg = bytearray('', encoding="utf-8")

    while True:

        root.update()

        data = c.recv(1024)

        if not data:

            print('Closing connection')
            conn_lock.release()
            break

        msg = msg + data

    print(msg.decode())

    T.insert(tk.END, msg.decode())

    root.update()

    c.close()


def runServer(s):

    root.update()

    T.delete("1.0", tk.END)

    conection, addr = s.accept()


    conn_lock.acquire()
    print('Connected to :', addr[0], ':', addr[1])

    start_new_thread(threaded, (conection,))

    root.after(10, runServer, s)

root = tk.Tk()

root.geometry("250x170")

T = tk.Text(root, height=8, width=52)

T.pack()

root.after(10, runServer, s)

root.mainloop()
