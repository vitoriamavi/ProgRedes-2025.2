import socket
import struct

HOST =''
PORT = 20000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Digite o nome do arquivo que deseja baixar: ")

client.send(bytes([len(filename)]))

client.send(filename.encode())

exists = client.recv(1)

if exists == b'\x00':
    print("Arquivo não encontrado no servidor.")
    client.close()
    quit()

print("Arquivo encontrado no servidor.")
size_data = client.recv(4)
filesize = struct.unpack('!I', size_data)[0]

print(f"Tamanho do arquivo: {filesize} bytes.")

received = 0
file_bytes = b''

while received < filesize:
    bloco = client.recv(4096)
    if not bloco: break
    file_bytes += bloco
    received += len(bloco)

with open(filename, 'wb') as f:
    f.write(file_bytes)

print(f"Arquivo {filename} baixado com sucesso.")
client.close()