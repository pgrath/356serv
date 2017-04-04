#cs356 client server
# by Pat McGrath
import sys,socket

#create master socket
mainSock = socket.socket()

def socketConnect(host, port):
    try:
        mainSock.bind((host, port)) #bind a socket
        servHstNM = socket.gethostname()
        print("Host "+ servHstNM + " connected successfully")
        return True
    except (s.error , msg): # print the error if there is one
        print ('Unable to bind to port! Got error: ' + str(msg[0]) + ' ' + msg[1])
        return False

#start listening for connections if the program is able to bind the port
if (socketConnect("localhost",55554)):
    try:
        mainSock.listen(5)
        print("Listening for connections. . .")
    except (s.error, msg):
        print("Listen error: "+ str(msg[0]) + ' ' + msg[1])

#begin main loop
while True:
    ##
    ## code for listening should go here
    ##
    client, addr = mainSock.accept() # accept connection from client


    ##
    ## code for sending should go here
    ##
