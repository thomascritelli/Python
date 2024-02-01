import socket
import json
from threading import Thread

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22004
BUFFER_SIZE = 1024


def ricevi_comandi(sock_service, addr_client):
    print("ricevo comandi da:", addr_client)
    with sock_service as sock_client:
        while True:
            data=sock_client.recv(BUFFER_SIZE).decode()
            if not data:
                break
            data = json.loads(data)
        
            primoNumero = data["primoNumero"]
            operazione = data["operazione"]
            secondoNumero = data["secondoNumero"]

            risultato = 0
            if operazione == '+':
                    risultato = primoNumero + secondoNumero
            elif operazione == '-':
                    risultato = primoNumero - secondoNumero
            elif operazione == '*':
                    risultato = primoNumero * secondoNumero
            elif operazione == '/':
                if secondoNumero != 0:
                    risultato = primoNumero / secondoNumero
                else:
                    "impossibile dividere per 0!"
            elif operazione == '%':
                risultato = primoNumero % secondoNumero

            sock_service.sendall((str(risultato)).encode())
    print("connessione con :", addr_client," chiusa")

def ricevi_connessioni(sock_listen):
     print("server in ascolto su: ", ((SERVER_ADDRESS, SERVER_PORT)))
     while True:
          sock_service,address_client = sock_listen.accept()
          print("connessione ricevuta da: ",address_client)
          print("creo un thread per servire le richieste")
          try:
               Thread(target=ricevi_comandi, args = (sock_service,address_client)).start()
          except:
               print("il thread non si avvia")
               sock_listen.close()

def avvio_server(indirizzo,porta):
     print("avvio in corso")
     try:
          sock_listen=socket.socket()
          sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
          sock_listen.bind((indirizzo,porta))
          sock_listen.listen(5)
          print("server avviato")
          ricevi_connessioni(sock_listen)
        
     except socket.error as errore:
          print("errore nell'avvio del server",errore)

if __name__ == '__main__':
    avvio_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")