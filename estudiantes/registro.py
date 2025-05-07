import csv

def cargar_estudiantes(ruta_csv):
    estudiantes_validos = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                nota = float(fila["nota"])
                if 0.0 <= nota <= 5.0:
                    estudiantes_validos.append({
                        "nombre": fila["nombre"],
                        "nota": nota
                    })
                else:
                    print(f"Nota fuera de rango para {fila['nombre']}: {nota}")
            except ValueError:
                print(f"Nota inválida para {fila['nombre']}: {fila['nota']}")
    return estudiantes_validos