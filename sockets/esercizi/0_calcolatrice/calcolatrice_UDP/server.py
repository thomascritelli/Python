import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("server in attesa di messaggi..")
while True:
    #ricezione dei dati dal client
    data= sock.recv(BUFFER_SIZE)
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    primoNumero = data['primoNumero']
    operazione = data['operazione']
    secondoNumero = data['secondoNumero']
    print(f"{primoNumero}{operazione}{secondoNumero}")
    
    if (operazione != '*' and operazione != '/' and operazione != '-' and operazione != '+'):
        print("Operatore inaccettabile")
    else:
        if (operazione == '*'):
            risultato = primoNumero*secondoNumero
        elif (operazione == '+'):
            risultato = primoNumero+secondoNumero
        elif (operazione == '-'):
            risultato = primoNumero-secondoNumero
        else:
            risultato = primoNumero/secondoNumero
    risultato = json.dumps(risultato)
    sock.sendto(risultato.encode(), (SERVER_IP, SERVER_PORT))