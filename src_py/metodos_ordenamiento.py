class MetodosOrdenamiento:
    def sort_Bubble(self, array):
        arreglo=array.copy()
        #print("metodo")
        n= len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]> arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self,array):
        arreglo=array.copy()
        n= len(arreglo)
        intercambio= True
        for i in range(n):
            if not intercambio:
                break
            intercambio=False
        
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambio = True 
        return arreglo

        

    def sort_seleccion(self, array):
        arreglo=array.copy()
        n = len(arreglo)
        for i in range(n):
            indice_minimo=i
            for j in range(i+1,n):
                if arreglo[j]>arreglo[indice_minimo]:
                    indice_minimo=j
                    arreglo[i],arreglo[indice_minimo]= arreglo[indice_minimo], arreglo[i]
        return arreglo


    def sort_shell(self, array):
        arreglo= array.copy()
        n= len(arreglo)
        gap=n//2
        
        while gap>0:
            for i in range(gap, n):
                temp= arreglo[i]
                j=i
                while j >= gap and arreglo [j - gap ]> temp:
                    arreglo[j]=arreglo[j- gap]
                    j-=gap
                arreglo[j]=temp
            gap//=2
        return arreglo
    
    def sort_inserccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(1, n):
            clave = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = clave
        return arreglo