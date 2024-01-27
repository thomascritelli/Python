import socket, json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    comando = input("Inserisci comando: ")
    parametri = []
    if comando != "list" and comando != "close":
        nomeStudente = input("Inserisci il nome e cognome dello studente").lower()
        nomeStudente = nomeStudente.strip()
        parametri.append(nomeStudente)
        if comando == "put":
            materia = input("Inserisci il nome della materia: ").lower().strip()
            
            voto = float(input("Inserisci il voto:"))
            
            ore = int(input("Inserisci il numero di ore per assenza: "))
        parametri.append(materia)
        parametri.append(voto)
        parametri.append(ore)
        
    comando = json.dumps(comando)
    parametri = json.dumps(input("Inserisci parametri: "))
    istruzioni = {
        'comando':comando,
        'parametri':parametri,
    }
    sock.sendto(comando.encode("UTF-8"),(SERVER_IP,SERVER_PORT))
    data = sock.recv(BUFFER_SIZE)
