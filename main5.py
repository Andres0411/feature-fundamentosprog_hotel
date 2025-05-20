from datetime import datetime

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
contador_procesos = 1 ## Se cambio contdor_reservas por contador_procesos ## Un proceso incluye desde la reserva, checkin y checkout
registro_operaciones = []
registro_titulares = []

def listar_habitaciones():
    print("\nListado de habitaciones:")
    for h in habitaciones:
        print(f'Hab. {h["No"]} - {h["Tipo"]}, Cap: {h["Capacidad"]}, Precio: S/.{h["Precio"]}, Estado: {estados[h["Estado"]]}')

def ver_disponibilidad():
    print("\nHabitaciones disponibles:")
    for h in habitaciones:
        if h["Estado"] == 1:
            print(f'Hab. {h["No"]} - Tipo: {h["Tipo"]} - Capacidad: {h["Capacidad"]} - Precio: S/.{h["Precio"]}')

def registrar_operacion(operacion, numero_habitacion, proceso_id):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro_operaciones.append({
        "ProcesoID": proceso_id,
        "Operacion": operacion,
        "Habitacion": numero_habitacion,
        "Fecha": fecha
    })

def reservar():
    global contador_procesos
    ver_disponibilidad()
    numero = input("\nIngrese el número de habitación a reservar: ")
    if not numero.isdigit():
        print("Entrada inválida. Ingrese un número válido.")
        return
    numero = int(numero)

    for h in habitaciones:
        if h["No"] == numero:
            if h["Estado"] == 1:
                nombre = input("Ingrese el nombre completo del titular: ").strip()
                dni = input("Ingrese el DNI del titular: ").strip()
                if nombre == "" or dni == "":
                    print("Datos incompletos. Proceso cancelado.")
                    return
                proceso_id = contador_procesos
                contador_procesos += 1
                h["Estado"] = 2
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                registro_titulares.append({
                    "ProcesoID": proceso_id,
                    "Habitacion": numero,
                    "DNI": dni,
                    "Nombre": nombre,
                    "Fecha": fecha
                })
                registrar_operacion("Reserva", numero, proceso_id)
                print(f"Habitación {numero} reservada exitosamente.")
                print(f"Número de proceso: {proceso_id}")
            else:
                print("La habitación no está disponible para reservar.")
            return
    print("Número de habitación no encontrado.")

def obtener_proceso_id_por_habitacion(habitacion_num):
    for titular in registro_titulares:
        if titular["Habitacion"] == habitacion_num:
            return titular["ProcesoID"]
    return None

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
            h["Estado"] = 3
            proceso_id = obtener_proceso_id_por_habitacion(numero)
            registrar_operacion("Check-in", numero, proceso_id)
            print(f"Check-in exitoso en la habitación {numero}.")
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
            proceso_id = obtener_proceso_id_por_habitacion(numero)
            registrar_operacion("Check-out", numero, proceso_id)
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
            proceso_id = obtener_proceso_id_por_habitacion(numero)
            registrar_operacion("Limpieza", numero, proceso_id)
            print(f"Habitación {numero} ha sido limpiada y ahora está libre.")
            return
    print("Número de habitación inválido o no está sucia.")

def ver_registro_operaciones():
    if not registro_operaciones:
        print("\nNo hay operaciones registradas.")
    else:
        print("\nHistorial de operaciones:")
        for r in registro_operaciones:
            print(f'{r["Fecha"]} - {r["Operacion"]} - Habitación {r["Habitacion"]} - Proceso #{r["ProcesoID"]}')

def obtener_estado_proceso(proceso_id):
    # Filtra las operaciones por ese proceso y obtiene la más reciente
    operaciones = [op for op in registro_operaciones if op["ProcesoID"] == proceso_id]
    if not operaciones:
        return "Sin operaciones"
    
    # Buscar manualmente la operación más reciente por fecha (como texto)
    ultima = operaciones[0]
    for op in operaciones[1:]:
        if op["Fecha"] > ultima["Fecha"]:  # comparación de strings funciona para este formato
            ultima = op
    
    if ultima["Operacion"] == "Reserva":
        return "Reservado"
    elif ultima["Operacion"] == "Check-in":
        return "Ocupado"
    elif ultima["Operacion"] == "Check-out":
        return "Sucia"
    elif ultima["Operacion"] == "Limpieza":
        return "Libre"
    else:
        return ultima["Operacion"]

def ver_titulares():
    if not registro_titulares:
        print("\nNo hay titulares registrados.")
        return
    print("\nListado de titulares de proceso:")
    for t in registro_titulares:
        estado = obtener_estado_proceso(t["ProcesoID"])
        print(f'Proceso #{t["ProcesoID"]} - Habitación {t["Habitacion"]} - {t["Nombre"]} (DNI: {t["DNI"]}) - Estado: {estado} - Fecha: {t["Fecha"]}')

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
        print("6. Ver historial de operaciones") 
        print("7. Ver titulares de reserva")  
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
            ver_registro_operaciones()
        elif opcion == 7:
            ver_titulares()
        elif opcion == 9:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()

