# Introdução a `Socket` e `cliente/servidor(TCP/UDP)`

**Biblioteca Socket**

> Fornece acesso de baixo nível à interface de rede.

> O S.O fornece a API socket que relaciona o programa com a rede

Permite que possamos controlar a abertura, fechamento e sincronização de conexões direto com a placa de rede.
Assim sendo possível criar um relacionamento com o nosso programa, sistema operacional e também com a placa de rede.

## Desenvolvimento de um cliente TCP

**Python security**

O TCP(Transmission Control, Protocol) ou protocolo de controle de transmissão é um dos protocolos de comunicação que dão suporte a rede global Internet, verificando se os dados são enviados na seqência correta e sem erros.

> O intuito do programa é verificar se os dados estão sendo enviados de maneira integra.

O cliente TCP ira enviar determinados dados ao servidor e irá retornar uma informção com os dados enviados, verificando se todos os dados foram enviados de maneira correta.
**Obedecendo o princípio da integridade**

## Desenvolvimento de um cliente UDP

O UDP(User Datagram Protocol) ou protocolo de datagrama do usuário é um protocolo simples da camada de transporte que permite que a aplicação envie um datagrama dentro de um pacote IPV4 ou IPV6 a um determinado destino, porém sem a garantia de que o pacote chegará corretamente.
**Aqui não possui o princípio da integridade, mas sim o de disponibilidade**
