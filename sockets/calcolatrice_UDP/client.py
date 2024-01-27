import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):
    #invio del messaggio al server
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = str(input("Inserisci l operazione: (+, -, *, /, %)"))
    secondoNumero = float(input("Inserisci il secondo numero: "))
    message = {
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero,
    }
    message = json.dumps(message)
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print("messaggio inviato al server...")

    #ricezione della risposta dal server
    data= sock.recv(BUFFER_SIZE)
    print(f"{data.decode()}")