import socket

HOST = "127.0.0.1"  
PORT = 54321  

def Menu(dato):
    if dato.startswith('/'):
        dato = dato[1:]
    comando = dato
    switch(comando)

def switch(comando):
    if comando == "exit":
        salir(comando)
    elif comando == "direccion":
        direccion()
    elif comando == "login":
        usuario()
    elif comando == "mute":
        mute()
    elif comando == "todos":
        todos()

def salir(comando):
    print(comando)
    exit()
def direccion():
    print("cliente pide direccion")
def usuario():
    print("cliente pide loguearse")
def mute():
    print("mute")
def todos():
    print("todos")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conectando desde {addr}")
        while True:
            data = conn.recv(1024)
            if data.decode('utf-8').startswith("/"):
                Menu(data.decode('utf-8'))
                print(f'Comando recibido!','Cliente dice:',data.decode('utf-8'))
                resp = input('Servidor:')
                conn.sendall(bytes(resp, encoding="ascii"))
            if data.decode('utf-8') == 'exit':
                conn.sendall(b'Conexion finalizada')
                break
