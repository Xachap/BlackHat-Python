import socket
import threading

# Asignamos IP y puerto al servidor
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

# Maximo numero de conexiones simultaneas: 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# Hilos para gestionar las peticiones de los clientes
def handle_client(client_socket):
    
    # Imprimimos lo que envia el cliente
    request = client_socket.recv(1024)
    print "[*] Received %s" % request
    
    # Respuesta para el cliente
    client_socket.send("ACK!")
    
    client_socket.close()
    
while True:
    client, addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    
    # Activamos el hilo de nuestro cliente para manejar los datos entrantes
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()