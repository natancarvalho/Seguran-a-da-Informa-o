#Buffer Overflow

Deve-se compilar o arquivo f.c sobre as seguintes condições:

gcc -shared -fno-stack-protector -o libmain.so -fPIC  f.c

Após compilado pode-se exucutar a aplicação listiner.py que aguardará dados que serão enviados pelo exploit.py
