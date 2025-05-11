import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
import datetime
from generar_arreglos import generar_arreglos_encadenados

if __name__ == "__main__":
    print("Iniciando el programa...")

    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 30000, 50000, 1000000]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        metodos_dicc = {
            "burbuja": metodosO.sort_Bubble,
            "burbuja mejorado": metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion": metodosO.sort_seleccion,
            "shell": metodosO.sort_shell,
            "inserccion": metodosO.sort_inserccion
        }

        for nombre, fun_metodo in metodos_dicc.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    print("\n--- Resultados de tiempo mediante los metodos de ordenamiento ---\n")
    for tam, nombre, tiempo_resultado in resultados:
        print(f'Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo_resultado:.6f} segundos')

    print("\n--- Arreglos generados ---\n")
    generar_arreglos_encadenados()

    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    titulo_general = f"Kevin Paladines, Daniel Cajas - {fecha_hora_actual}"

    tiempos_by_metodos = {
        "burbuja": [],
        "burbuja mejorado": [],
        "seleccion": [],
        "shell": [],
        "inserccion": []
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodos[nombre].append(tiempo)

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodos.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparativa de tiempos para cada método de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.suptitle(titulo_general, fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.xticks(tamanios)
    plt.show()
