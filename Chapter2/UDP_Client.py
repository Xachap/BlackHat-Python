import socket

target_host = "127.0.0.1"
target_port = 4096

# Creamos el socket
### AF_INET -> IPv4 estandar
### SOCK_DGRAM -> indica que es un cliente UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviamos datos de prueba
client.sendto("PUEBAAAA",(target_host,target_port))

# Recibimos la respuesta
data, addr = client.recvfrom(4096)

print data

client.close()

