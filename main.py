"""
Sistema de Gestión de Eventos Culturales - Fundación CultuVivo (MVP básico)
"""

from datetime import datetime

TIPOS_BOLETO = ["General", "VIP", "Preferencial"]

# Datos en memoria
eventos = []   # cada evento: {"id", "nombre", "fecha", "lugar", "capacidad"}
reservas = []  # cada reserva: {"evento_id", "identificacion", "nombre", "correo", "boleto", "estado"}


# ---------------------------------------------------------------
# Entradas validadas
# ---------------------------------------------------------------
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("  Error: no puede estar vacío.")


def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("  Error: debe ser mayor a cero.")
        except ValueError:
            print("  Error: ingrese un número entero.")


def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            datetime.strptime(texto, "%Y-%m-%d %H:%M")
            return texto
        except ValueError:
            print("  Error: use el formato AAAA-MM-DD HH:MM (ej: 2026-12-15 19:30).")


def pedir_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo.split("@")[-1]:
            return correo
        print("  Error: correo inválido.")


def pedir_boleto():
    while True:
        print("Tipo de boleto: 1. General  2. VIP  3. Preferencial")
        opcion = input("Elija (1-3): ").strip()
        if opcion in ["1", "2", "3"]:
            return TIPOS_BOLETO[int(opcion) - 1]
        print("  Error: opción inválida.")


# ---------------------------------------------------------------
# Lógica de eventos y reservas
# ---------------------------------------------------------------
def buscar_evento(id_evento):
    for e in eventos:
        if e["id"] == id_evento:
            return e
    return None


def buscar_reserva(id_evento, identificacion):
    for r in reservas:
        if r["evento_id"] == id_evento and r["identificacion"] == identificacion:
            return r
    return None


def contar(id_evento, estado):
    total = 0
    for r in reservas:
        if r["evento_id"] == id_evento and r["estado"] == estado:
            total += 1
    return total


def promover_lista_espera(evento):
    """Si hay cupo, pasa a Confirmado a los que están En espera (por orden de llegada)."""
    for r in reservas:
        if contar(evento["id"], "Confirmado") >= evento["capacidad"]:
            break
        if r["evento_id"] == evento["id"] and r["estado"] == "En espera":
            r["estado"] = "Confirmado"
            print(f"  -> {r['nombre']} ({r['identificacion']}) pasó de 'En espera' a 'Confirmado'.")


def listar_eventos():
    if len(eventos) == 0:
        print("  (No hay eventos registrados)")
        return
    for e in eventos:
        confirmados = contar(e["id"], "Confirmado")
        print(f"  [{e['id']}] {e['nombre']} | {e['fecha']} | {e['lugar']} | "
              f"Aforo: {confirmados}/{e['capacidad']}")


# ---------------------------------------------------------------
# Administrador
# ---------------------------------------------------------------
def crear_evento():
    id_evento = pedir_texto("ID del evento: ")
    if buscar_evento(id_evento) is not None:
        print("  Error: ya existe un evento con ese ID.")
        return
    nombre = pedir_texto("Nombre: ")
    fecha = pedir_fecha("Fecha y hora (AAAA-MM-DD HH:MM): ")
    lugar = pedir_texto("Lugar: ")
    capacidad = pedir_entero_positivo("Capacidad máxima: ")
    eventos.append({"id": id_evento, "nombre": nombre, "fecha": fecha,
                    "lugar": lugar, "capacidad": capacidad})
    print("  Evento creado correctamente.")


def modificar_evento():
    listar_eventos()
    evento = buscar_evento(pedir_texto("ID del evento a modificar: "))
    if evento is None:
        print("  Error: el evento no existe.")
        return
    evento["nombre"] = pedir_texto("Nuevo nombre: ")
    evento["fecha"] = pedir_fecha("Nueva fecha y hora (AAAA-MM-DD HH:MM): ")
    evento["lugar"] = pedir_texto("Nuevo lugar: ")
    nueva_capacidad = pedir_entero_positivo("Nueva capacidad máxima: ")
    if nueva_capacidad < contar(evento["id"], "Confirmado"):
        print("  Error: la capacidad es menor que las reservas ya confirmadas. Capacidad sin cambios.")
    else:
        evento["capacidad"] = nueva_capacidad
        promover_lista_espera(evento)
    print("  Evento actualizado.")


def cambiar_estado():
    listar_eventos()
    id_evento = pedir_texto("ID del evento: ")
    evento = buscar_evento(id_evento)
    if evento is None:
        print("  Error: el evento no existe.")
        return
    identificacion = pedir_texto("Identificación del asistente: ")
    reserva = buscar_reserva(id_evento, identificacion)
    if reserva is None:
        print("  Error: no hay reserva para esa identificación en este evento.")
        return
    print(f"  Estado actual: {reserva['estado']}")
    print("Nuevo estado: 1. Confirmado  2. En espera  3. Cancelado")
    opcion = input("Elija (1-3): ").strip()
    if opcion == "1":
        if reserva["estado"] != "Confirmado" and contar(id_evento, "Confirmado") >= evento["capacidad"]:
            print("  Error: no hay aforo disponible.")
            return
        reserva["estado"] = "Confirmado"
    elif opcion == "2":
        reserva["estado"] = "En espera"
        promover_lista_espera(evento)
    elif opcion == "3":
        reserva["estado"] = "Cancelado"
        promover_lista_espera(evento)
    else:
        print("  Error: opción inválida.")
        return
    print(f"  Estado actualizado a: {reserva['estado']}")


def menu_admin():
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Crear evento")
        print("2. Modificar evento")
        print("3. Listar eventos")
        print("4. Cambiar estado de una reserva")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            crear_evento()
        elif opcion == "2":
            modificar_evento()
        elif opcion == "3":
            listar_eventos()
        elif opcion == "4":
            cambiar_estado()
        elif opcion == "0":
            return
        else:
            print("  Opción inválida.")


# ---------------------------------------------------------------
# Asistente
# ---------------------------------------------------------------
def inscribir_asistente():
    listar_eventos()
    id_evento = pedir_texto("ID del evento: ")
    evento = buscar_evento(id_evento)
    if evento is None:
        print("  Error: el evento no existe.")
        return
    identificacion = pedir_texto("Número de identificación: ")
    previa = buscar_reserva(id_evento, identificacion)
    if previa is not None and previa["estado"] != "Cancelado":
        print("  Error: ya tiene una inscripción activa en este evento.")
        return
    nombre = pedir_texto("Nombre completo: ")
    correo = pedir_correo()
    boleto = pedir_boleto()

    if contar(id_evento, "Confirmado") < evento["capacidad"]:
        estado = "Confirmado"
    else:
        estado = "En espera"

    if previa is not None:  # volvió a inscribirse después de cancelar
        previa.update({"nombre": nombre, "correo": correo, "boleto": boleto, "estado": estado})
    else:
        reservas.append({"evento_id": id_evento, "identificacion": identificacion,
                         "nombre": nombre, "correo": correo, "boleto": boleto, "estado": estado})

    print("\n  Inscripción registrada:")
    print(f"    Evento: {evento['nombre']} ({evento['fecha']}, {evento['lugar']})")
    print(f"    Asistente: {nombre} - {identificacion}")
    print(f"    Boleto: {boleto}")
    print(f"    Estado: {estado}")


def consultar_inscripciones():
    identificacion = pedir_texto("Número de identificación: ")
    encontradas = [r for r in reservas if r["identificacion"] == identificacion]
    if len(encontradas) == 0:
        print("  No se encontraron inscripciones con esa identificación.")
        return
    for r in encontradas:
        e = buscar_evento(r["evento_id"])
        print(f"  {e['nombre']} | {e['fecha']} | {e['lugar']} | {r['boleto']} | {r['estado']}")


def cancelar_inscripcion():
    identificacion = pedir_texto("Número de identificación: ")
    id_evento = pedir_texto("ID del evento: ")
    reserva = buscar_reserva(id_evento, identificacion)
    if reserva is None or reserva["estado"] == "Cancelado":
        print("  Error: no hay una inscripción activa con esos datos.")
        return
    reserva["estado"] = "Cancelado"
    print("  Inscripción cancelada.")
    promover_lista_espera(buscar_evento(id_evento))


def menu_asistente():
    while True:
        print("\n--- MENÚ ASISTENTE ---")
        print("1. Inscribirme a un evento")
        print("2. Consultar mis inscripciones")
        print("3. Cancelar una inscripción")
        print("4. Ver eventos")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            inscribir_asistente()
        elif opcion == "2":
            consultar_inscripciones()
        elif opcion == "3":
            cancelar_inscripcion()
        elif opcion == "4":
            listar_eventos()
        elif opcion == "0":
            return
        else:
            print("  Opción inválida.")


# ---------------------------------------------------------------
# Reportes
# ---------------------------------------------------------------
def reporte_aforo():
    if len(eventos) == 0:
        print("  (No hay eventos registrados)")
        return
    print(f"\n  {'Evento':<22}{'Cap.':>5}{'Conf.':>7}{'Espera':>8}{'Canc.':>7}{'Ocup.':>8}")
    for e in eventos:
        conf = contar(e["id"], "Confirmado")
        esp = contar(e["id"], "En espera")
        canc = contar(e["id"], "Cancelado")
        ocupacion = conf * 100 / e["capacidad"]
        print(f"  {e['nombre'][:20]:<22}{e['capacidad']:>5}{conf:>7}{esp:>8}{canc:>7}{ocupacion:>7.1f}%")


def reporte_boletos():
    for tipo in TIPOS_BOLETO:
        total = 0
        for r in reservas:
            if r["boleto"] == tipo and r["estado"] != "Cancelado":
                total += 1
        print(f"  {tipo:<14}{total}")


def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Aforo y ocupación por evento")
        print("2. Inscripciones activas por tipo de boleto")
        print("0. Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            reporte_aforo()
        elif opcion == "2":
            reporte_boletos()
        elif opcion == "0":
            return
        else:
            print("  Opción inválida.")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
def main():
    while True:
        print("\n=== FUNDACIÓN CULTUVIVO - EVENTOS CULTURALES ===")
        print("1. Administrador")
        print("2. Asistente")
        print("3. Reportes")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            menu_admin()
        elif opcion == "2":
            menu_asistente()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("  Opción inválida.")


main()