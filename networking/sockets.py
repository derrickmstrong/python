# Sockets - Networking

# Create simple web browser
import socket # REQUIRED

# Create socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # connect socket with 2 parameters: 1) url 2)port number to web server

# Send connection
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Loop
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

# Close connection
mysock.close() 
