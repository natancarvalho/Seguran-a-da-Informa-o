# Trabalho 2 - Anatomia de um ataque (PortScan)

Primeiramente foi construído um port scan em Python 3 para analisar as portas abertas em algum endereço IP conhecido aguardando a resposta lara saber que serviço estaria rodando.
Foram analizados IPs conhecidos e públicos do Departamento de Engenharia Eletrônica e de Computação da UFRJ. As portas checadas estavam entre 1 e 1024.
Não se obteve resposta de que tipo de serviço estaria rodando nessas portas. Como substituto ao Nessus - erro durante a instalação - foi utilizado NMAP já contido no Kali Linux e o resultado foi exatamente o mesmo encontrado pelo port scan desenvolvido pelo grupo.

Sabe-se ainda que a porta 3128 dos IPs testados estavam abertas para serviço de SSH, entretanto as respostas não foram obtidas também pelo port scan.
Outra característica interessante foi constatar que as máquinas do departamento não respondem a pedidos ICMP para evitar técnicas de mapeamento de topologia.

Não há patches a serem proposto segundo o CVE.
