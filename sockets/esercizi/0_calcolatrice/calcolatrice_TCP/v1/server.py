import socket
import json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))
    sock_server.listen()
    print("Attesa del client...")

    while True:
        sock_service, address_client = sock_server.accept()
        data=sock_service.recv(BUFFER_SIZE)
        if not data:
            break
        with sock_service as sock_client:
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

                sock_service.sendall((str(risultato)).encode())
            
            print(risultato)  