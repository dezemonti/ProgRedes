import socket
import threading

HOST = "127.0.0.1"
PORT = 54321

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(name=f'Cliente {addr}',target=client_thread, args=(conn,addr))
            print(f"Se conectó {thread.name}")
            thread.start()

def client_thread(conn, addr):
    clientThread = threading.current_thread().name
    try:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if data == '/chau':
                conn.sendall(b'Conexion finalizada')
                break
            if data.startswith("/"):
                print(f'Comando recibido! {clientThread} dice:', data)
                resp = input('Servidor:')
                print(f'Esperando mensaje del Cliente...')
                conn.sendall(bytes(resp, encoding='utf-8'))
    except Exception as e:
        print(f"Error cuando se manejaba el cliente: {e}")
    finally:
        conn.close()
        print(f"Conexion al Cliente ({addr[0]}:{addr[1]}) cerrada")

server()