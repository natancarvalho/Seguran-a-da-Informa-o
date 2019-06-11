# Buffer Overflow

Foi usado um exploit desenvolvido em Python para conectar-se a um socket e enviar uma string codificada em UTF-8 para um exemplo de aplicação em C pássível de stack overflow encontrada no site da OWASP.

O exploit foi baseado no primeiro trabalho feito na disciplina em que era necessário estabelecer uma comunicação entre máquinas para enviar um pacote criptografado, recebê-lo e decriptografar. A função principal envia primeiramente um valor multiplicado por 10 até que seja "estourado" a pilha de memória. 

A função em main.c apenas recebe um vetor de 10 posições e armazena em memória sem nenhum tratamento prévio. Essa função é executada dentro de um código em python baseado também no receptor implementado no primeiro trabalho da displina.

Deve-se compilar o arquivo f.c sobre as seguintes condições:

gcc -shared -fno-stack-protector -o libmain.so -fPIC  main.c

Após compilado pode-se exucutar a aplicação "aplicacao.py" que aguardará dados que serão enviados pelo exploit.py


Referência:

https://www.owasp.org/index.php/Buffer_Overflows#Stack_Overflow
