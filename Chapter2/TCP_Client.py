# Cliente TCP
import socket

target_host = "127.0.0.1"
target_port = 9999

# Creamos un socket
### AF_INET -> IPv4 estandar
### SOCK_STREAM -> indica que es un cliente TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el cliente
client.connect((target_host,target_port))

# Enviamos datos de prueba
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Recibimos la respuesta
response = client.recv(4096)

print response

client.close()