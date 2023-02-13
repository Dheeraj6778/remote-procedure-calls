code="""
from server_procedures import *
# Server
import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9998

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    msg_from_client = clientsocket.recv(1024).decode('utf-8')
    #print(msg_from_client)
    lst = msg_from_client.split(' ')
    procedure_name=lst[0]
    lst=lst[1:]
    #print(lst)
    temp_lst=[]
    flag=0
    for x in lst:
        if is_int(x)==False:
            st=f'\" {x} \"'
            temp_lst.append(st)
            pass
        else:
            temp_lst.append(x)
    #print(temp_lst)
    param_string=None
    if len(lst[0])==0:
        param_string = procedure_name+"("+','.join(lst)+')'
    else:
        param_string = procedure_name+"("+','.join(temp_lst)+')'
    #print(param_string)
    val=eval(param_string)
    msg_to_client=f"message to client from server is {val}"
    clientsocket.send(msg_to_client.encode('ascii'))
    clientsocket.close()

"""
fp=open('rpc_server.py','w')
fp.write(code)
fp.close()