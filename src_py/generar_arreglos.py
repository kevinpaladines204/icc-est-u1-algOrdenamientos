import random

def generar_arreglos_encadenados():
    arreglo_5000 = [random.randint(0, 99999) for _ in range(5000)]
    print("Arreglo de 5000: ")
    print(arreglo_5000)

    arreglo_10000 = arreglo_5000.copy() + [random.randint(0, 99999) for _ in range(5000)]
    print("\nArreglo de 10000: ")
    print(arreglo_10000)

    arreglo_30000 = arreglo_10000.copy() + [random.randint(0, 99999) for _ in range(10000)]
    print("\nArreglo de 30000: ")
    print(arreglo_30000)

    arreglo_50000 = arreglo_30000.copy() + [random.randint(0, 99999) for _ in range(30000)]
    print("\nArreglo de 50000: ")
    print(arreglo_50000)

    arreglo_100000 = arreglo_50000.copy() + [random.randint(0, 99999) for _ in range(50000)]
    print("\nArreglo de 100000: ")
    print(arreglo_100000)
if __name__ == "__main__":
    generar_arreglos_encadenados()