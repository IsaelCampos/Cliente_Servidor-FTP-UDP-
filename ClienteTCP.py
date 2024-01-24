import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e: 
        print("A conexão falhou")
        print("Erro: {}".format(e))  
        sys.exit()

    print("Socket criado com sucesso")

    # Vamos realizar uma conexão tcp e ip
    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = int(input("Digite a porta a ser conectada: "))  

    try:
        s.connect((HostAlvo, PortaAlvo))
        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + " na porta: " + str(PortaAlvo))
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
