import socket, json, time
import tkinter as tk
from tkinter import ttk

SERVER_IP = '127.0.0.1'
SERVER_PORT = 22004
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

username = ""
password = ""
for i in range(5):
    
    print("Per registrazione inserire due volte '0'")
    username = input("inserisci username: ")
    password = input("inserisci password: ")

    if username == "0" and password == "0":
        password1 = "1"
        while password != password1:
            username = input("inserisci un username: ")
            password = input("inserisci una password: ")
            password1 = input("conferma la password: ")
        comando = "registrazione"
        query = f"INSERT INTO `utenti`(`cod_utente`, `username`, `password`) VALUES ('','{username}','{password}');"
    else:
        comando = "login"
        query = f"SELECT * FROM utenti WHERE username = '{username}' AND password = '{password}';"
    istruzioni = {
        'comando': comando,
        'query': query,
    }
    
    istruzioni = json.dumps(istruzioni)
    sock.sendto(istruzioni.encode("UTF-8"), (SERVER_IP,SERVER_PORT))
    data = sock.recv(BUFFER_SIZE)
    
    
    data = data.decode()
    risp = data['risp']
    results = data['results']

    
    print("Risposta dal server:", data)

while True:
    """
    Chiedere login per accedere al programma (deciderò poi se via riga di comando o graficamente), 
    -> finestra in cui vi è una lista di elementi che rappresentano gli account
        -> selezionando un account si riempiranno le label con i dati
    """
    
