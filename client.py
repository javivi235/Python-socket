#!/usr/bin/env python3

import socket

import tkinter as tk

def runClient():

    HOST = '192.168.0.109'
    PORT = 9999

    msg = T.get("1.0", tk.END)

    print("sending: ", msg)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode('utf-8'))

        s.close()


root = tk.Tk()

root.geometry("250x170")

T = tk.Text(root, height=8, width=52)

T.pack()

startButton = tk.Button(root, text="Enviar Mensaje", command=runClient)
startButton.pack()

tk.mainloop()


