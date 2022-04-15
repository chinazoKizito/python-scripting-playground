import socket


# socket set up
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket connected to a host on a port number
mysock.connect(("data.pr4e.org", 80))
command = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(command)

# loop to receive and decode data across the net and close the socket
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

