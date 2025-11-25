import socket
import os
from xmlrpc import client

HOST = ''
PORT = 5000
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nome_arquivo = input("Digite o nome do arquivo: ")

    client.sendto(nome_arquivo.encode(), (HOST, PORT))
    exists, _ = client.recvfrom(1)
    if exists == b'0':
        print("Arquivo não encontrado no servidor.")
        return
    print("Arquivo encontrado no servidor.")

    tamanho_arquivo, _ = client.recvfrom(4096)
    tamanho_arquivo = int(tamanho_arquivo.decode())
    print(f"Tamanho do arquivo: {tamanho_arquivo} bytes.")

    bytes_recebidos = 0
    saida = "recebido_" + nome_arquivo

    with open(saida, 'wb') as f:
        while bytes_recebidos < tamanho_arquivo:
            dados, _ = client.recvfrom(4096)
            f.write(dados)
            bytes_recebidos += len(dados)

    print(f"Arquivo {saida} recebido.")

if __name__ == "__main__":
    main()
