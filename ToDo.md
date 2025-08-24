## client.py
- [x] Conectarse al servidor (IP, puerto).
- [x] Enviar nombre al servidor.
- [x] Enviar comandos (`hit`, `stand`, `help`, etc.).
- [ ] Mejorar interacción en consola (mostrar cartas de todos los jugadores, no solo respuestas del servidor).
- [ ] Formato más bonito en los mensajes recibidos.


## server.py
- [x] Escuchar conexiones en un puerto.
- [x] Crear un hilo por cliente conectado.
- [x] Recibir nombre y registrar jugador en backend.
- [ ] Repartir 2 cartas cuando entra.
- [ ] Implementar turnos por orden de llegada.
- [ ] Enviar a todos los clientes el estado actual de la partida (broadcast).
- [ ] Implementar lógica de crupier (pedir hasta 17 o pasarse).
- [ ] Decidir y enviar resultado final a todos los jugadores.

---

## blackjack.py
- [x] Clase `Player` (nombre, mano, total, estado).
- [x] Método para pedir carta (`hit`).
- [ ] Dar opcion de elegir valor de As (1 u 11).
- [ ] Revisar si jugador ya ganó o perdió y actualizar estado.
- [ ] Implementar acción `stand` (guardar que el jugador no quiere más cartas).
- [ ] Implementar acción `split` (si recibe dos cartas iguales).
- [ ] Función para reiniciar jugador (nueva partida).
- [ ] Lógica del mazo completo (52 cartas) en vez de solo 1–11.
- [ ] Clase `Dealer` (crupier con reglas propias).

---

## README.md
- [ ] Explicar requisitos (Python 3).
- [ ] Explicar instalación y ejecución (`server.py`, `client.py`).
- [ ] Explicar comandos disponibles.
- [ ] Explicar arquitectura básica (cliente ↔ servidor ↔ backend).
- [ ] Agregar ejemplo de sesión (correr cliente y servidor).
