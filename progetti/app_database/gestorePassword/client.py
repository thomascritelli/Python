import socket, json 
import tkinter as tk
from tkinter import ttk

SERVER_IP = '127.0.0.1'
SERVER_PORT = 22004
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

while True:
    """
    Chiedere login per accedere al programma (deciderò poi se via riga di comando o graficamente), 
    -> finestra in cui vi è una lista di elementi che rappresentano gli account
        -> selezionando un account si riempiranno le label con i dati
    """