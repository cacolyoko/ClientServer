import socket

#Guardo el número de expediente como str
num_exp = input("Introduce tu número de expediente: ")

#Creo el socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecto a la IP y el puerto
client.connect(('127.0.0.1', 1369))

#Codifico el valor de str a bytes y lo envío por el socket al servidor
num_exp = num_exp.encode()
client.send(num_exp)

#Recibo un valor en bytes y lo imprimo decodificándolo
recibir = client.recv(8)
print('>>', recibir.decode())