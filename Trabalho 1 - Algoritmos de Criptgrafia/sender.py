import socket
import time
from simplecrypt import encrypt, decrypt

PATH = "./socket/"
CLIENT = ''
PORT = 9000
KEY = "L45P1"

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
        s.send(bytes(encrypt(KEY, data)))
        end = time.time()
        print (end - start)

start = time.time()
if __name__ == '__main__':
  main()

