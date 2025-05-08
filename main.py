# Integracion de las funciones en un solo archivo

from estudiantes import registro

if __name__ == "__main__":
    ruta_csv = "estudiantes.csv"
    estudiantes = registro.cargar_estudiantes(ruta_csv)
    registro.mostrar_estudiantes_tabla(estudiantes)
    promedio = registro.promedio_estudiantes(estudiantes)
    print(f"Promedio de notas: {promedio:.2f}")
