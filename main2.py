# Datos iniciales
habitaciones = [
    {"No": 101, "Capacidad": 2, "Tipo": "Matrimonial", "Estado": 1, "Precio": 500},
    {"No": 102, "Capacidad": 2, "Tipo": "Doble", "Estado": 1, "Precio": 600},
    {"No": 103, "Capacidad": 1, "Tipo": "Simple", "Estado": 3, "Precio": 300},
    {"No": 104, "Capacidad": 1, "Tipo": "Simple", "Estado": 2, "Precio": 300},
    {"No": 105, "Capacidad": 3, "Tipo": "Triple", "Estado": 1, "Precio": 700},
    {"No": 106, "Capacidad": 3, "Tipo": "Triple", "Estado": 3, "Precio": 700},
]

estados = {
    1: "Libre",
    2: "Reservado",
    3: "Ocupado",
    4: "Sucia"
}

# Arreglo adicional para registrar ocupantes
ocupantes = []  # Cada elemento será: {"No": 101, "NombreCompleto": "Juan Pérez"}


# Funciones
def listar_habitaciones():
    print("\nListado de habitaciones:")
    for h in habitaciones:
        print(f'Hab. {h["No"]} - {h["Tipo"]}, Cap: {h["Capacidad"]}, Precio: S/.{h["Precio"]}, Estado: {estados[h["Estado"]]}')

def ver_disponibilidad():
    print("\nHabitaciones disponibles:")
    for h in habitaciones:
        if h["Estado"] == 1:
            print(f'Hab. {h["No"]} - Tipo: {h["Tipo"]} - Capacidad: {h["Capacidad"]} - Precio: S/.{h["Precio"]}')

def reservar():
    ver_disponibilidad()
    numero = input("\nIngrese el número de habitación a reservar: ")
    if not numero.isdigit():
        print("Entrada inválida. Ingrese un número válido.")
        return
    numero = int(numero)
    for h in habitaciones:
        if h["No"] == numero:
            if h["Estado"] == 1:
                h["Estado"] = 2
                print(f"Habitación {numero} reservada exitosamente.")
            else:
                print("La habitación no está disponible para reservar.")
            return
    print("Número de habitación no encontrado.")

# Función para listar ocupantes actuales
def listar_ocupantes():
    if not ocupantes:
        print("\nNo hay ocupantes registrados actualmente.")
        return
    print("\nOcupantes registrados:")
    for o in ocupantes:
        print(f'Hab. {o["No"]} - Nombre: {o["NombreCompleto"]}')

# Modificamos el check-in para registrar nombre completo
def checkin():
    print("\nHabitaciones reservadas disponibles para check-in:")
    reservadas = [h for h in habitaciones if h["Estado"] == 2]
    if not reservadas:
        print("No hay habitaciones reservadas.")
        return
    for h in reservadas:
        print(f'Hab. {h["No"]} - Tipo: {h["Tipo"]}')
    numero = input("\nIngrese el número de habitación para hacer check-in: ")
    if not numero.isdigit():
        print("Entrada inválida. Ingrese un número válido.")
        return
    numero = int(numero)
    for h in reservadas:
        if h["No"] == numero:
            nombre = input("Ingrese el nombre completo del ocupante: ").strip()
            if nombre == "":
                print("Nombre no puede estar vacío.")
                return
            h["Estado"] = 3
            ocupantes.append({"No": numero, "NombreCompleto": nombre})
            print(f"Check-in exitoso en la habitación {numero} para {nombre}.")
            return
    print("Número de habitación inválido o no reservada.")


def checkout():
    print("\nHabitaciones ocupadas disponibles para check-out:")
    ocupadas = [h for h in habitaciones if h["Estado"] == 3]
    if not ocupadas:
        print("No hay habitaciones ocupadas.")
        return
    for h in ocupadas:
        print(f'Hab. {h["No"]} - Tipo: {h["Tipo"]}')
    numero = input("\nIngrese el número de habitación para hacer checkout: ")
    if not numero.isdigit():
        print("Entrada inválida. Ingrese un número válido.")
        return
    numero = int(numero)
    for h in ocupadas:
        if h["No"] == numero:
            h["Estado"] = 4
            print(f"Check-out realizado. Habitación {numero} ahora está sucia.")
            return
    print("Número de habitación inválido o no ocupada.")

def mantenimiento():
    print("\nHabitaciones sucias disponibles para limpieza:")
    sucias = [h for h in habitaciones if h["Estado"] == 4]
    if not sucias:
        print("No hay habitaciones sucias en este momento.")
        return
    for h in sucias:
        print(f'Hab. {h["No"]} - Tipo: {h["Tipo"]}')
    numero = input("\nIngrese el número de habitación a limpiar: ")
    if not numero.isdigit():
        print("Entrada inválida. Ingrese un número válido.")
        return
    numero = int(numero)
    for h in sucias:
        if h["No"] == numero:
            h["Estado"] = 1
            print(f"Habitación {numero} ha sido limpiada y ahora está libre.")
            return
    print("Número de habitación inválido o no está sucia.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú del Hotel ---")
        print("0. Listar todas las habitaciones")
        print("1. Ver disponibilidad")
        print("2. Reservar")
        print("3. Check-in")
        print("4. Check-out")
        print("5. Mantenimiento")
        print("6. Ver ocupantes actuales")  # NUEVA OPCIÓN
        print("9. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("Opción no válida. Intente nuevamente.")
            continue

        opcion = int(opcion)

        if opcion == 0:
            listar_habitaciones()
        elif opcion == 1:
            ver_disponibilidad()
        elif opcion == 2:
            reservar()
        elif opcion == 3:
            checkin()
        elif opcion == 4:
            checkout()
        elif opcion == 5:
            mantenimiento()
        elif opcion == 6:
            listar_ocupantes()
        elif opcion == 9:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
