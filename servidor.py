import socket

#Creo el socket en el servidor con su IP y puerto
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 1369))

#Mantengo la conexión con el socket
serv.listen(5)
clientsocket, address = serv.accept()
print("Socket activo y corriendo con una conexión de", address)

#Recibo datos del socket proveniente del cliente
data = clientsocket.recv(8).decode()
print("Received data", data)

#Transformo los bytes en un valor integer y lo opero, después lo vuelvo a cambiar a str y lo codifico en bytes
temp = int(data) * 2
temp = str(temp)

#Envío el valor al socket del cliente
clientsocket.send(temp.encode())