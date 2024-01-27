import socket, sys, random, os, time, threading, multiprocessing, json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 10
BUFFER_SIZE = 1024

def genera_richieste(num, address, port):
    start_time_thread = time.time()
    try:
        sock = socket.socket()
        sock.connect((address, port))
        print(f"\n{threading.current_thread().name}{num+1}) Connessione al server: {address}:{port}")
    except:
        print("Il thread non si avvia")
        sys.exit()
    comandi = ['+','-','*','/','%']
    primoNumero = random.randint(1,100)
    operatore = comandi[random.randint(1,100)]
    secondoNumero = random.randint(1,100)

    messaggio = {
        'primoNumero':primoNumero,
        'operatore':operatore,
        'secondoNumero':secondoNumero,
    }
    messaggio = json.dumps(messaggio)
    sock.sendall(messaggio.encode("UTF-8"))
    data = sock.recv(BUFFER_SIZE)
    print(f"Risultato: {data.decode()}")

    end_time_thread = time.time()
    print(f"{threading.current_thread().name}) tempo di esecuzione: {end_time_thread - start_time_thread}")




if __name__ == '__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste, args = (SERVER_ADDRESS, SERVER_PORT)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print(f"Total threads time= {end_time - start_time}")