import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999
#to start we pass in the IP address and port we want the server to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5) #tells the server to listen with a max backlog of connections set to 5

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#this is our client-handling threading
#when a client connects we receive the socket into the client variable and the remote connection details in the addr variable.
def handle_client(client_socket):
    #print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    # send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while true:

    client,addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
