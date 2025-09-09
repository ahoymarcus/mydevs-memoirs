i# Criando e Configurando uma Rede com QoS (OSPF e MPLS)
 
Olá, neste projeto do Curso de **Rede de Computadores** da faculdade IESB, eu tenho o desafio de criar e configurar uma rede de uma empresa como QoS, de modo que para a obtenção desse resultado serão usados os protocolos OSPF e MPLS, ademais, serão usandos como base para este projeto o sistema operacional Debian Linux e a aplicação de simulação de redes da CISCO PacketTracer.


Requisitos do Projeto:

1. **Criar três LANs para representar as três filiais de uma empresa**
2. **Usar roteamento dinâmico OSPF: IPv4 e IPv6**
3. **Configura MPLS**
4. **Aplicar QoS para priorizar videoconferência e chamadas de voz**


![](./public/)


<br>

## Construindo o Projeto

Como determinam os requisitos para este projeto, a topografia básica desta rede da empresa deve ter pelo menos três LANs para representar cada uma das redes locais das filiais da empresa, de forma que o primeiro passo, então, para este projeto fora construir separadamente cada uma das LANs individualmente.


<br>

### Criando a Topologia Básica das LANs da Empresa

Assim, para dar partida na construção dessa infraestrutura de rede das filiais, fora utilizado um switch que liga alguns hosts a um roteador gateway para representar cada uma dessas LANs.


O procedimento utilizado fora de se escolher os ícones de computadores desktops, switchs e roteador, no PacketTracre da Cisco, para fazer manualmente a conexão de cada dispositivo, lembrando que parte dos requisitos deste projeto é que fossem utilizados endereçamento IPv4 e IPv6.


Dessa forma, cada um dos hosts fora conectado ao switch por meio de cabos **Straight-Through**, nas portas FastEthernet, enquanto cada swicht fora ligado ao seu roteador de gateway por meio das portas GigaEthernet.  


Ademais, para que cada host pudesse receber endereços privados IPv4 e IPv6, fora preciso mudar as configurações dos hosts de endereçamento estático para endereçamento dinâmico por meio do protocolo DHCP:
 
![Configurando o endereçamento IPv4 e IPv6 por DHCP](./public/enderecamento-dinamico-dhcp.png)


<br>

Podemos ver a seguir que não apenas os endereços privados foram configurados pelo servidor DHCP, como a conexão já estaria pronta, tendo sido testada por meio do comando ping:

```
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::210:11FF:FE52:7087
   IPv6 Address....................: ::
   Autoconfiguration IPv4 Address..: 169.254.112.135
   Subnet Mask.....................: 255.255.0.0
   Default Gateway.................: ::
                                     0.0.0.0

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0

C:\>ping 169.254.2.120

Pinging 169.254.2.120 with 32 bytes of data:

Reply from 169.254.2.120: bytes=32 time<1ms TTL=128
Reply from 169.254.2.120: bytes=32 time<1ms TTL=128
Reply from 169.254.2.120: bytes=32 time<1ms TTL=128
Reply from 169.254.2.120: bytes=32 time<1ms TTL=128

Ping statistics for 169.254.2.120:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

![Testando a conexão entre os hosts com o comando Ping](./public/testando-a-conexao-dos-host-com-ping.png)


<br>

Contudo, como pode ser visto nesta próxima imagem geral da topologia da empresa, podemos observar que os roteadores, via de regra, vem com as suas portas ou interfaces desativadas por padrão por razões de administração, de modo que essas interfaces precisam ser ligadas manualmente a partir da CLI.

![Visão geral da Topologia da rede das LANs com os roteadores com suas interfaces desabilitadas](./public/visao-geral-da-topologia-das-lans-com-roteadores-desabilitados.png)


<br>

Nesse sentido, temos abaixo a imagem com a configuração no terminal CLI de um dos roteadores os comandos necessários para abilitar a porta/interface da rede interna da LAN: 

![Configurando a Interface interna do Roteador por meio da CLI](./public/configurando-a-interface-interna-lan-do-roteador-na-cli.png)

```
Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface GigabitEthernet0/0/0
Router(config-if)#no shutdown

Router(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
```


<br>

Finalmente, vermos a imagem com a visão geral da topologia da empresa com cada uma de suas três LANs plenamente funcionais!

![Visão geral da Topologia da rede das LANs com os roteadores com suas interfaces abilitadas](./public/visao-geral-da-topologia-das-lans-com-roteadores-abilitados.png)


<br>

### Fazendo a Conexão dos Roteadores Gateway das LANs da Empresa 

A primeira tarefa a ser feita para pode iniciar a interligação das três LANs das filias da empresa seria decidir sobre o design do uso dos roteadores para o projeto da rede.


Nesse caso, a ideia seria de se adicionar um roteador para cada filial para que eles pudessem fazer o papel de **roteadores de borada**, este roteadores que seriam, então, conectados uns aos outros da rede da empresa, enquanto o roteador original permanecendo apenas como um roteador Gateway simple para a sua respectiva LAN.


Duas razões que tratam de **Boas Práticas** poderiam justificar essa escolha:

1. **Melhorar a redundância da topologia**
2. **Melhorar a escalabilidade da rede**


Nesse sentido, no caminho de preparar os roteadores Gateway de cada LAN para se conectarem à rede principal da empresa, elas precisam primeiramente fazer uma expansão para adicionar novo módulo de portas para as conexões necessárias.


Os passos para fazer a modança são:

1. **Desligar os roteadores**
2. **Buscar na Aba Physical de sua interface o novo módulo desejado: NIM-ES2-4**


A razão pela escolha desse módulo em particular, **NIM-ES2-4**, tem haver com a topologia mais simples da rede sendo criada, que precisa apenas das portas extras para poder completar todas as conexão necessárias! 

> [!IMPORTANT]
> Após desligar o roteador e fazer a adição do novo módulo, é importante reativar as portas novamente, da mesma forma que fora feito anteriormente neste projeto! 




![](./public/)
![](./public/)


<br> 

##






![](./public/)
![](./public/)
![](./public/)


<br>

##





![](./public/)
![](./public/)
![](./public/)


<br>

## Outros links:

 - [linkedin:] https://www.linkedin.com/in/marcus-vinicius-richa-183104199/
 - [Github:] https://github.com/ahoymarcus/
 - [My Old Web Portfolio:] https://redux-reactjs-personal-portfolio-webpage-version-2.netlify.app/


















