#cs356 client server
# by Pat McGrath
import sys,socket

#master connection list
topology = [[0,1,3,7],
            [1,0,1,99],
            [3,1,0,2],
            [7,99,2,0]]

def bellman(main[x][z],com[c][v]):
    


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

    rouTable = topology[0] # to make this router 0
    ##
    ## code for listening should go here
    ##
    client, addr = mainSock.accept() # accept connection from client


    ##
    ## code for sending should go here
    ##
