import pickle
import socket
import sys

#Function to print tables
def printTable(table):
    print("DESTINATION-------INTERFACE------LINKCOST")
    for i in table:
        if i[1] == -1:
            print("    ",i[0],"            ",i[1],"           ",i[2])
        elif i[1]==MAXINT:
            print("    ",i[0],"            inf            inf")
        else:
            print("    ",i[0],"            ",i[1],"            ",i[2])


#Used to represent infinity
MAXINT = sys.maxsize

#Initialize/Print intial table at node1
table1 = [[0,0,1],[1,-1,0],[2,1,1],[3,MAXINT,MAXINT]]
printTable(table1)

#Create socket variables
s = socket.socket()
port = 57171
host = ''

try:
    s.bind((host,port))
except (s.error, msg):
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

#Wait to receive table from node0
print('Socket bind complete')
s.listen(1)

#Receive the table from node0
client, addr = s.accept()
print ('Got connection from', addr)
table0 = client.recv(1024)
table0 = pickle.loads(table0)

#Print both tables
print("Current table: ")
printTable(table1)
print("Received table: ")
printTable(table0)

#Perform calculations
num = 0
len1 = len(table1)
len2 = len(table0)
for i in range(len1):
    for j in range(len2):
        num = table1[i][2] + int(table0[j][2])
        if num<table0[i][2]:
            table0[i][2] = num+1

print("Updated table: ")
printTable(table0)

client.send(pickle.dumps(table0))
s.close()

    
