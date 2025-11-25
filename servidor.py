import socket
import os

HOST = ''
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Aguardando resposta do cliente...")

while True:
    nome_arquivo, endereco = server.recvfrom(4096)
    nome_arquivo = nome_arquivo.decode()

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado.")
        server.sendto(b'0', endereco)
        print("Arquivio não encontrado no servidor.")
        continue
    
    else:
        server.sendto(b'1', endereco)

        tamanho_arquivo = os.path.getsize(nome_arquivo)
        server.sendto(str(tamanho_arquivo.encode(), endereco))
        print(f"Enviando arquivo {nome_arquivo} de tamanho {tamanho_arquivo} bytes.")

        with open(nome_arquivo, 'rb') as f:
            while True:
                dados = f.read(4096)
                if not dados:
                    break
                server.sendto(dados, endereco)

        print(f"Arquivo {nome_arquivo} enviado para o endereço {endereco}.")


if __name__ == "__main__":
    main()