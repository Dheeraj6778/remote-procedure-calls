import socket
def foo(par_1):
   clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = socket.gethostname()
   port = 9998
   clientsocket.connect((host, port))
   message = f'foo {par_1}'
   clientsocket.sendall(message.encode('utf-8'))
   data = clientsocket.recv(1024).decode('utf-8')
   clientsocket.close()
   return data
def bar(par_1,par_2):
   clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = socket.gethostname()
   port = 9998
   clientsocket.connect((host, port))
   message = f'bar {par_1} {par_2}'
   clientsocket.sendall(message.encode('utf-8'))
   data = clientsocket.recv(1024).decode('utf-8')
   clientsocket.close()
   return data
def random_rating():
   clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = socket.gethostname()
   port = 9998
   clientsocket.connect((host, port))
   message = f'random_rating '
   clientsocket.sendall(message.encode('utf-8'))
   data = clientsocket.recv(1024).decode('utf-8')
   clientsocket.close()
   return data
