from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:


    def __init__(self):
        print ('Benchmarking instanciado')
        
    def medir_tiempo(self, funcion, arreglo):
        inicio= time.perf_counter()
        funcion(arreglo)
        fin=time.perf_counter()
        return fin-inicio
        
    def build_arreglo(self, tamano):
        arreglo= []
        for _ in range (tamano):
            numero=random.randint(0,99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicio= time.time()
        tarea()
        fin= time.time()
        return(fin - inicio)
        

    def contar_con_nano(self, tarea):
        inicio= time.time_ns()
        tarea()
        fin= time.time_ns()
        return(fin-inicio)/1_000_000_000