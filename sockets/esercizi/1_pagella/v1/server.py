import socket, json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 22004
BUFFER_SIZE = 1024

diz = {'antonio barbera': [['matematica', 8, 1], ['italiano', 6, 1], ['inglese', 9.5, 0], ['storia', 8, 2], ['geografia', 8, 1]],
       'giuseppe gullo': [['matematica', 9, 0], ['italiano', 7, 3], ['inglese', 7.5, 4], ['storia', 7.5, 4], ['geografia', 5, 7]],
       'nicola spina': [['matematica', 7.5, 2], ['italiano', 6, 2], ['inglese', 4, 3], ['storia', 8.5, 2], ['geografia', 8, 2]],
      }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))
    sock_server.listen()
    print("Attesa del client...")
    sock_service, address_client = sock_server.accept()
    while True:
        data = sock_service.recv(BUFFER_SIZE)
        richiesta = ""
        if not data:
            break
        else:
            data = data.decode()
            data = json.loads(data)

            comando = data['comando']
            parametri = data['parametri']

            if comando == "list":
                richiesta = diz
                risp = "OK"
                
            elif comando == "get":
                if parametri[0] in diz:
                    richiesta = diz[parametri[0]]
                    risp = "OK"
                    print(diz[parametri[0]])
                else:
                    risp = "Studente non trovato!"

            elif comando == "set":
                if parametri[0] in diz:
                    risp = "Studente già presente!"
                else:
                    diz[parametri[0]] = parametri[1:]
                    risp = "Studente aggiunto"
            
            elif comando == "put":
                
                    materia = parametri[1]
                    voto = parametri[2]
                    ore = parametri[3]
                    if parametri[0] in diz:
                        diz[parametri[0]].append([materia, voto, ore])
                        risp = "Studente Aggiornato"
                    else:
                        risp = "Studente non trovato!"

            risposta = {
                'risp':risp,
                'richiesta':richiesta,
            }

            sock_service.sendall(json.dumps(risp).encode())
