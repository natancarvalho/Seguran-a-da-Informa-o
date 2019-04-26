import socket
import time
from Crypto.Cipher import AES

# Encryption
PATH = "./socket/"
CLIENT = '10.10.11.116'
PORT = 9000
KEY = b"L45P1L45P1L45P12"

# Main
def main ():
    # Initialize socket
    print ("Initializing socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((CLIENT, PORT))
    print ("Connection initialized!")
    while True:
        data = input("> ")
        start = time.time()
        encryption_suite = AES.new(KEY, AES.MODE_CBC, 'This is an IV456')
        cipher_text = encryption_suite.encrypt(data)
        end = time.time()
        print (end - start)
        s.send(bytes(cipher_text))


if __name__ == '__main__':
  main()

# Decryption
#decryption_suite = AES.new(KEY, AES.MODE_CBC, 'This is an IV456')
#plain_text = decryption_suite.decrypt(cipher_text)
