import socket
import os

HOST = ''
PORT = 5000

nome_arquivo = input("Digite o nome do arquivo: ")

client.sendto(nome_arquivo.encode(), (HOST, PORT))
