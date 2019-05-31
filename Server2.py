import threading
import time
import queue
import socket

#funciona suma
def suma(num, output_queue): 
    total = 0
    #suma los 875 numeros con un tiempo de espera de un segundo
    for x in range (0,875):
        total = total + num
        time.sleep(1)
    
    if (output_queue.empty() == False):
        total = total + int(output_queue.get())
    #guarda el resultado en una cola
    output_queue.put(total)
    return total

#suma los totales de cada nodo
def suma_total(val1, val2, val3, val4):
    return val1+val2+val3+val4

#programa del servidor para recibir datos
def server_program():
    # get the hostname
    host = '127.0.0.1' #ip del host
    port = 5555  #puerto de transmisión de datos

    server_socket = socket.socket()  # instanciar socket

    server_socket.bind((host, port))  

    #configurar cuantos clientes se pueden conectar simultaneamente
    #en este caso solo se necesita 1, pero igualmente se definen 2
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceptar nueva conexion
    print("Conexión desde: " + str(address)) #muestra datos de la conexion
    while True:
        # recibe datos, no mayores a 1024 bytes
        data = conn.recv(1024).decode()
        aux = data.split(',') #separa los datos por comas original = 1,2,3,4 - después del split = [1,2,3,4] 
        aux_queue = queue.Queue()
        aux_queue.put(aux[0])
        aux_queue.put(aux[1])
        aux_queue.put(aux[2])
        aux_queue.put(aux[3])

        my_queue = queue.Queue() #inicia la cola
        #crea los hilos de ejecución, estos emulan los nodos (servidores de computo)
        #estos hilos llaman a la función suma y le dan los parametros necesarios, 
        # en este caso el numero y la cola en donde almacenar el resultado
        t1 = threading.Thread(target=suma, args=(int(aux_queue.get()),my_queue))
        t2 = threading.Thread(target=suma, args=(int(aux_queue.get()),my_queue))
        t3 = threading.Thread(target=suma, args=(int(aux_queue.get()),my_queue))
        t4 = threading.Thread(target=suma, args=(int(aux_queue.get()),my_queue)) 
        t1.start()
            
        t2.start() 
                
        t3.start() 
                     
        t4.start()
        # inicia los hilos de ejecucion
        
        # espera hasta que todos los hilos estén ejecutados
        t1.join() 
        t2.join() 
        t3.join()
        t4.join()

        #llama a la fución suma_total, dandole de parametros los valores almacenados en la cola
        #total2 = suma_total(my_queue.get(), my_queue.get(), my_queue.get(), my_queue.get())
        total_final = my_queue.get()
        print(total_final)

        print("Terminado!")
        if not data:
            # if data is not received break
            break
        #imprime la información del cliente
        print("desde el cliente: " + str(data))

        conn.send(str(total_final).encode())  # envía el total de la suma al cliente

    conn.close()  # cierra la conexión


if __name__ == '__main__':
    server_program()

  


 