import socket

HOST = "127.0.0.1"  # dominio  o IP del servidor
PORT = 54321  # el puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("Cliente:")
    print(f'Esperando mensaje del Servidor...')
    if msg.startswith("/"):
        s.sendall(bytes(msg, encoding="ascii"))
        data = s.recv(1024)
        while data:
            if data.decode('utf-8').startswith("/"):
                print(f'Comando recibido!','Servidor dice:',data.decode('utf-8'))
                msg = input("Cliente:")
                print(f'Esperando mensaje del Servidor...')
                s.sendall(bytes(msg, encoding="ascii"))
                data = s.recv(1024)
                if msg == "exit":
                    break