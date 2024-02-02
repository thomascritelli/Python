from configparser import SectionProxy
from email.headerregistry import MessageIDHeader
import socket, sys, random, os, time, threading, multiprocessing, json


NUM_WORKER = 5
SERVER_ADDRESS = "192.168.9.50"
SERVER_PORT = 22004

def genera_richieste(SERVER_ADDRESS, SERVER_PORT):

    try:
        start_time_threads=time.time()
        s=socket.socket()
        s.connect((SERVER_ADDRESS,SERVER_PORT))
        print(f"\n{threading.current_thread().name} connessione al server: {SERVER_ADDRESS}:{SERVER_PORT}")
    except:
        print(f"\n{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    comandi=['+','-','*','/']
    primoNumero=random.randint(1,100)
    operazione=comandi[random.randint(0,3)]
    secondoNumero=random.randint(1,100)

    messaggio={'primoNumero':primoNumero,
               'operazione':operazione,
               'secondoNumero':secondoNumero}
    
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    
    print(f"\n {threading.current_thread().name} ",messaggio)
    print(f"\n {threading.current_thread().name}risultato: ", data.decode())

    #s.close()
    end_time_thread=time.time()
    print(f"\n{threading.current_thread().name} execution time = ", end_time_thread - start_time_threads)

if __name__ == '__main__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste, args=(SERVER_ADDRESS, SERVER_PORT)) for _ in range(NUM_WORKER)] 
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("\n total threads time= ", end_time - start_time)