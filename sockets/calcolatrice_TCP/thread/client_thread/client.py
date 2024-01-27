import socket, json
SERVER_IP = "127.0.0.1"
SERVER_PORT = 22004
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"In attesa dei dati da inviare a: {SERVER_IP}:{SERVER_PORT}")

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

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((SERVER_IP, SERVER_PORT))
        sock_service.sendto(message.encode("UTF-8"), (SERVER_IP,SERVER_PORT)) # invio direttamente in formato byte
        print("In attesa di risposta...")
        data = sock_service.recv(1024)
    print("risultato: ",data.decode())