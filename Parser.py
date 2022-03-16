import sys
import socket

URL_PREFIX = sys.argv[1].replace("unfs://","")


host = socket.gethostbyname(socket.gethostname())
print("Connecting to UNFS File Server...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((URL_PREFIX,4443))
DATA = s.recv(5000)
s.close()