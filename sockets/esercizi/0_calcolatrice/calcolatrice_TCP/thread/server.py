import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22004

def ricevi_comandi(sock_service, addr_client):
    with sock_service as sock_client:
        while True:
            data = sock_client.recv(1024)
            if not data:
                break
            
            data=data.decode()
            data=json.loads(data)
            primoNumero=data['primoNumero']
            operazione=data['operazione']
            secondoNumero=data['secondoNumero']

            if(operazione != 'x' and operazione != '+' and operazione != '-' and operazione != '/'):
                print("operatore non accettabile")
                break
            else:
                if(operazione == 'x'):
                    risultato=primoNumero*secondoNumero
                elif(operazione == '+'):
                    risultato=primoNumero+secondoNumero
                elif(operazione == '-'):
                    risultato=primoNumero-secondoNumero
                else:
                    risultato=primoNumero/secondoNumero
                sock_client.sendall(str(risultato).encode())
            print(f"Invio dei dati calcolati a {addr_client}")
            print("Chiusura connessione...")

def ricevi_connessioni(sock_listen, indirizzo, porta):
    while True:
        sock_service, address_client = sock_listen.accept()
        try:
            print(f"Connesso con: {indirizzo}:{porta}")
            Thread(target = ricevi_comandi, args = (sock_service, address_client)).start()
        except:
            sock_listen.close()

def avvia_server(indirizzo, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
        sock_server.bind((indirizzo, porta))
        sock_server.listen()
        ricevi_connessioni(sock_server, indirizzo, porta)

print("In attesa di connessione...")
avvia_server(SERVER_ADDRESS, SERVER_PORT)


