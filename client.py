import socket
import pickle
import sys

MAXINT = sys.maxsize

#Initialize cost table
table0 = [[0,-1,0],[1,0,1],[2,1,3],[3,2,7]]

def printTable(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for i in table:
        if i[1] == -1:
            print("    ",i[0],"            ",i[1],"           ",i[2])
        elif i[1]==MAXINT:
            print("    ",i[0],"            inf            inf")
        else:
            print("    ",i[0],"            ",i[1],"            ",i[2])

printTable(table0)

s = socket.socket()

host = "afsconnect2.njit.edu"
port = 57171

s.connect((host, port))

#msg = input('Client: ')

#s.send(msg.encode())
s.send(pickle.dumps(table0))

#print (s.recv(1024).decode())

tab_update = s.recv(1024)
tab_update = pickle.loads(tab_update)

printTable(tab_update)

s.close
print ('Client: Connection closed')

#dumps
#loads
