import socket
import os
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 20000

server.bind((HOST, PORT))
server.listen(5)

print("Aguardando conexão com cliente...")

while True:
    client, addr = server.accept()
    print(f"Conectado a {addr}")

    size_bytes = client.recv(1)
    if not size_bytes:
        client.close()
        continue

    size = size_bytes[0]

    filename = client.recv(size).decode()
    print(f"Cliente {addr} solicitou o arquivo: {filename}")

    if not os.path.exists(filename):
        client.send(b'\x00')
        client.close()
        continue

    client.send(b'\x01')

    f = open(filename, 'rb')
    data = f.read()
    f.close()

    filesize = len(data)
    client.send(struct.pack('!I', filesize))
    client.sendall(data)

    print(f"Arquivo enviado com sucesso.")
    client.close()
    