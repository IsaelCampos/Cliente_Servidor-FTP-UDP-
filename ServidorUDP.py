import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")

host = 'localhost'
porta = 5432

## Utilizando o "s.bind" para fazer a ligação entre cliente/servidor

s.bind((host, porta))
mensagem = 'Servidor: Olá cliente!!, tudo em paz'

## O bind retornará "TRUE" quando estabelecer a conexão

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviado mensagem...")
        s.sendto(dados+(mensagem.encode()), end)