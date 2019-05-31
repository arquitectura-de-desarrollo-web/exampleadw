import socket


def cliente():
    host = '127.0.0.1'  # ip de destino (server)
    port = 5555  # puerto donde se envían los datos

    client_socket = socket.socket()  # instanciar socket
    client_socket.connect((host, port))  # conexión al servidor

    message = '1,2,3,4'  # mensaje a enviar, en este caso los 4 numeros para cada nodo

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # enviar mensaje
        data = client_socket.recv(1024).decode()  # recibir respuesta

        print('Respuesta del servidor: ' + data)  # mostrar respuesta

        #message = input(" -> ")  # again take input

    client_socket.close()  # cerrar la conexión


if __name__ == '__main__':
    cliente()
