# ============================================================#
#         INSTITUTO TECNOLÓGICO SUPERIOR PROGRESO             #
#                                                             #
#                      Carrera:                               #
#         Ingeniería en Sistemas Computacionales              #
#                                                             #
#                      Materia:                               #
#               Lenguajes y automatas I                       #
#                                                             #
#                     Actividad:                              #
#        Tarea 3: Castores afanosos programado                #
#                                                             #
#                      Docente:                               #
#               Ulises Morales Ramirez                        #
#                                                             #
#                       Alumno:                               #
#            David Ezequiel Caballero González                #
#                                                             #
#                  Fecha de entrega:                          #
#              Jueves 19 de marzo de 2026                     #             
# ============================================================#



from collections import deque # Del módulo collections, se trae solo la herramienta llamada deque
                              # Deque es una estructura de datos que permite agregar y eliminar 
                              # elementos de ambos extremos de manera eficiente. 
                              # Es útil para simular la cinta infinita de una Máquina de Turing, 
                              # ya que se puede expandir fácilmente en ambas direcciones.


# Función que simula la Máquina de Turing para los castores afanosos                                                       
def castores_afanosos(transitions, max_steps=10000): 

    cinta = deque([0])  # Aqui se define el estado inicial de la cinta, en este caso comienza en |0|
    posicion = 0        # Aqui se define la posición inicial del cabezal en la cinta
    estado = 'A'        # Aqui se define con que estado inicia la máquina, en este caso es el estado 'A'
    pasos = 0           # Aqui se define un contador de pasos
                                                                            
    while estado != 'H' and pasos < max_steps:                                  # La función castores_afanosos simula una Máquina de Turing  
        symbol = cinta[posicion]                                                # (Busy Beaver) utilizando una cinta infinita representada 
        write, move, estado = transitions[(estado, symbol)]                     # por un deque. La función toma un diccionario de transiciones              
                                                                                # que define el comportamiento de la máquina, y un número máximo 
        cinta[posicion] = write  # Aqui se escribe en la cinta |1| o |0|        # de pasos para evitar bucles infinitos. La máquina comienza en 
                                 # dependiendo de la transición.                # un estado inicial y sigue las transiciones hasta alcanzar un 
        if move == 'D':                                                         # estado de parada ('H') o agotar los pasos permitidos. Al final, 
            posicion += 1                                                       # se cuenta el número de unos en la cinta y se muestra el resultado.
            if posicion == len(cinta): # Aqui se amplia la cinta a la derecha
                cinta.append(0)        # cuando el cabezal llega al final de 
                                       # la cinta agregando un nuevo espacio 
                                       # con valor |0| al final de la cinta                                                                        
        
        else:                          # En cambio, si el movimiento es hacia la izquierda ('I'),
            if posicion == 0:          # aqui se amplia la cinta a la izquierda
                cinta.appendleft(0)    # cuando el cabezal llega al inicio de la cinta
            else:                      # agregando un nuevo espacio con valor |0|  
                posicion -= 1          # al inicio de la cinta

        pasos += 1

    unos = cinta.count(1)              # Aqui se cuenta el número de unos en la cinta después de que la máquina se detiene
    
    print(f"Pasos: {pasos} | Unos en cinta: {unos}") # Aqui se muestra el número de pasos que tomó la máquina para detenerse y 
                                                     # la cantidad de unos en la cinta al final de la ejecución
    
    print(f"Cinta: {list(cinta)}")     # Aqui se muestra el estado final de la cinta después de que la máquina se detiene,
    
    return pasos, unos            # Y aqui se devuelve el número de pasos y la cantidad de unos en la cinta como resultado de la función


# Configuración de las transiciones para los castores afanosos de 2, 3 y 4 estados

# ==== Castores afanosos de 2 estados ====
ca2 = {
    ('A', 0): (1, 'D', 'B'),
    ('A', 1): (1, 'I', 'B'),
    ('B', 0): (1, 'I', 'A'),
    ('B', 1): (1, 'D', 'H'),
}

# ==== Castores afanosos de 3 estados ====
ca3 = {
    ('A', 0): (1, 'D', 'B'),
    ('A', 1): (1, 'I', 'C'),
    ('B', 0): (1, 'I', 'A'),
    ('B', 1): (1, 'D', 'B'),
    ('C', 0): (1, 'I', 'B'),
    ('C', 1): (1, 'D', 'H'),
}

# ==== Castores afanosos de 4 estados ====
ca4 = {
    ('A', 0): (1, 'D', 'B'),
    ('A', 1): (1, 'I', 'B'),
    ('B', 0): (1, 'I', 'A'),
    ('B', 1): (0, 'I', 'C'),
    ('C', 0): (1, 'D', 'H'),
    ('C', 1): (1, 'I', 'D'),
    ('D', 0): (1, 'D', 'D'),
    ('D', 1): (0, 'D', 'A'),
}

# Ejecución de cada configuración de castores afanosos
print("=== Castores afanosos de 2 estados ===")
castores_afanosos(ca2)

print("\n=== Castores afanosos de 3 estados ===")
castores_afanosos(ca3)

print("\n=== Castores afanosos de 4 estados ===")
castores_afanosos(ca4)