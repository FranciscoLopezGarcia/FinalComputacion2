import socket
import threading
from blackjack import Blackjack

HOST = '0.0.0.0'
PORT = 22225

# Un único juego por ahora (backend)
juego = Blackjack()

def manejo_cliente(conection, address):
    print(f"Conexión establecida con {address}")
    conection.sendall(b"Conectado al servidor. Ingrese su nombre:\n")

    nombre = conection.recv(1024).decode().strip()
    jugador = juego.add_player(nombre)   # Registrar en backend
    conection.sendall(f"Bienvenido {nombre}!\n".encode())

    while True:
        try:
            data = conection.recv(1024)
            if not data:
                break

            comando = data.decode().strip().lower()
            respuesta = juego.process_command(jugador, comando)
            conection.sendall(respuesta.encode())
        except:
            break

    print(f"Cliente {address} desconectado")
    conection.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[INFO] Servidor escuchando en {HOST}:{PORT}")

    while True:
        conection, address = server.accept()
        hilo = threading.Thread(target=manejo_cliente, args=(conection, address))
        hilo.start()

if __name__ == "__main__":
    main()
