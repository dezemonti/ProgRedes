import socket

HOST = "127.0.0.1"  
PORT = 54321  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conectando desde {addr}")
        while True:
            data = conn.recv(1024)
            if data.decode('utf-8').startswith("/"):
                print(f'Comando recibido!','Cliente dice:',data.decode('utf-8'))
                resp = input('Servidor:')
                conn.sendall(bytes(resp, encoding="ascii"))
            if data.decode('utf-8') == 'exit':
                conn.sendall(b'Conexion finalizada')
                break