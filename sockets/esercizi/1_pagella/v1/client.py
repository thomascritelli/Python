import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 22004
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

while True:
    comando = input("Inserisci comando: ")
    parametri = []
    materia = ""
    voto = 0
    ore = 0

    if comando != "list" and comando != "close":
        nomeStudente = input("Inserisci il nome e cognome dello studente: ").lower()

        if comando == "put":
            materia = input("Inserisci il nome della materia: ").lower().strip()
            voto = float(input("Inserisci il voto:"))
            ore = int(input("Inserisci il numero di ore per assenza: "))
        parametri.extend([nomeStudente, materia, voto])

    else:
        if comando == "close":
            break
    istruzioni = {
        'comando': comando,
        'parametri': parametri,
    }
    istruzioni = json.dumps(istruzioni)
    sock.sendto(istruzioni.encode("UTF-8"), (SERVER_IP,SERVER_PORT))
    data = sock.recv(BUFFER_SIZE)
    
    data = data.decode()
    data = json.loads(data)
    risp = data['risp']
    richiesta = data['richiesta']
    print(richiesta)
    
    print("Risposta dal server:", data)