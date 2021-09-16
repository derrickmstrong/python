# Sockets - Networking
import socket # REQUIRED

# Example connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # connect socket with 2 parameters: 1) url 2)port number

