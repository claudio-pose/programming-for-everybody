import socket

# Open socket on port 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Get intro-short.txt file from server
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

# Output the server's response
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()