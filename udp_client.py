import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC, (target_host,target_port)")

#receive some data
data, addr = cliet.recvfrom(4096)

print data

#As you can see, we change the socket type to SOCK_DGRAM when creating the socket object. The next step is to simply call sendto() passing in the data and the server you want to send the data to. Because UDP is a connectionless protocol, there is no call to connect() beforehand. The last step is to call recvfrom() to receive the UDP data back. You will also notice that it returns both the data and the details of the remote host and port. 
