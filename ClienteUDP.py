from base64 import encode
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente socket criado com sucesso!")

host = 'localhost'
porta = 5432
mensagem = 'Olá servidor, tudo bem?'

try:
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))
    encode()
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print("Cliente: fechando conexão")
    s.close()