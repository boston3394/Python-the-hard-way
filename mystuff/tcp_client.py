import socket
#socket is the core module for creating networked servers and clients
target_host = "www.google.com"

target_port = 80 #http

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET paramenter specifies a standard IPv4 address or host name
#SOCK_STREAM indicates that it will be a TCP client

#connect the client
client.connect((target_host,target_port))
#sends the client to connect to www.google.com on port 80 as specified earlier

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response

#this is the simpliest form of TCP client but the one you write most often. 
