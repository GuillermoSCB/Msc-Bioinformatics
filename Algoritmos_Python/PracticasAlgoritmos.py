################################################################################################
################ Funciones correspondientes a los ejercicios del Entregable 2 ##################
################################################################################################


######## EJERCICIO 1

from itertools import combinations

def CalculaDX(posCortes):
    """
    (list) -> list
    Dada una lista de puntos de corte, calcula el tamaño de todos los posibles fragmentos generados.
        Entrada: lista de puntos de corte (números enteros). Incluye la posición 0 y el máximo tamaño de un fragmento M (igual a la longitud de la secuencia de ADN)
        Salida: lista de números enteros con los tamaños de todos los fragmentos de restricción posibles.
    >>> coords = [0, 4, 5]
    >>> CalculaDX(coords)
    [1, 4, 5]
    """

    combinaciones = combinations(posCortes, 2) # 2 porque quiero todas las posibles parejas de numeros 
    DX = [comb[1] - comb[0] for comb in combinaciones] # Según la doc: r-length tuples, in sorted order, no repeated elements, por eso resto el segundo menos el primero, están ordenados
    
    return(sorted(DX))






######## EJERCICIO 2

def MapaRestriccionesBusquedaExhaustiva(n, L):
    """
    (int, list) -> list 
    Dado el número de puntos de corte y las longitudes de los fragmentos producidos, calcula todas las posibles soluciones de las coordenadas de los puntos de corte.
        Entrada: número de puntos de corte (incluyendo las posiciones 0 y M) y lista de longitudes de fragmentos.
        Salida: lista de soluciones (tuplas) con las coordenadas de los puntos de corte.
    >>> n = 3
    >>> L = [2, 3, 5]
    >>> MapaRestriccionesBusquedaExhaustiva(n, L)
    [(0, 2, 5), (0, 3, 5)]
    """
    
    long_max = sorted(L)[-1] # también podría haber calculado el máximo de la lista en vez de ordenarla y coger el último elemento
    posiciones = list(range(0, long_max+1)) # posibles posiciones, no necesitaba poner el 0, long_max + 1 para que incluya M

    combinaciones = combinations(posiciones, n) # combinaciones de tantos puntos de corte como haya indicado en n. MEJORA: fijar 0 y M, combinaciones con n-2 números intermedios distintos de 0 y M

    X = [comb for comb in combinaciones if CalculaDX(comb) == L] # guardo posiciones de corte si las longitudes de fragmentos generados coinciden con L

    return X






######## EJERCICIO 3

def MapaRestriccionesBusquedaExhaustivaOptimizada(n, L):
    """
    (int, list) -> list 
    Dado el número de puntos de corte y las longitudes de los fragmentos producidos, calcula todas las posibles soluciones de las coordenadas de los puntos de corte.
        Entrada: número de puntos de corte (incluyendo las posiciones 0 y M) y lista de longitudes de fragmentos.
        Salida: lista de soluciones (listas) con las coordenadas de los puntos de corte.
    >>> n = 3
    >>> L = [2, 3, 5]
    >>> MapaRestriccionesBusquedaExhaustivaOptimizada(n, L)
    [[0, 2, 5], [0, 3, 5]]
    """

    pos_ini = 0
    pos_fin = sorted(L)[-1] # o max(L)
    pos_centrales = list(set((L)))[:-1] # Sobran paréntesis en la L. Quita duplicados y el último valor de la lista (el mayor si L está ordenado)

    combinaciones = combinations(pos_centrales, n-2)

    X = []
    for comb in combinaciones:
        posiciones = [pos_ini] + list(comb) + [pos_fin] # posicion ini + combinación + M
        if CalculaDX(posiciones) == L: # si coincide con L
            X.append(posiciones) # guardo coordenadas

    return(X)






######## EJERCICIO 4

from time import time
def TiempoEjecucion(func, *args):
    """
    (function, list) -> float 
    Calcula el tiempo de ejecución de una función en segundos.
        Entrada: nombre de la función y lista de argumentos.
        Salida: tiempo de ejecución en segundos.
    """
    inicio = time()
    func(*args)
    fin = time()
    return(fin-inicio)




######## EJERCICIO 5

def CalculaPrefijo(secuencia):
    """
    (list) -> int 
    Dada una lista de números enteros, calcula hasta qué posición la lista está ordenada de menor a mayor.
        Entrada: lista de números enteros.
        Salida: número entero con la última posición ordenada de la lista (siendo 1 la primera posición).
    >>> sec = [1, 2, 3, 6, 4, 5]
    >>> CalculaPrefijo(sec)
    3
    """

    minimo = min(secuencia)
    prefijo = 0

    if secuencia[0] == minimo: # Si el primer valor está ordenado
        prefijo = 1
        
        for i in range(len(secuencia)-1): 
            if secuencia[i+1] - secuencia[i] == 1: # Si el siguiente valor también está ordenado
                prefijo += 1
            else: 
                return(prefijo)
    return prefijo



def OrdenacionInversionSimple(permutacionInicial):
    """
    (list) -> int 
    Calcula las inversiones que deben realizarse en una secuencia de números para ordenarla.
        Entrada: lista de números enteros con la permutación inicial.
        Salida: lista de inversiones (tuplas de dos enteros) que permiten obtener la permutación identidad a partir de permutacionInicial. Los elementos de las tuplas son la coordenada de inicio y fin de la región a invertir (0-based).
    >>> pI = [1, 2, 3, 6, 4, 5]
    >>> OrdenacionInversionSimple(pI)
    [(3, 4), (4, 5)]
    """
    n = len(permutacionInicial)
    permutacion = permutacionInicial
    prefijo = CalculaPrefijo(permutacionInicial) 
    
    inversiones = []

    while prefijo < n: 
        ult_ord = prefijo

        for i in range(prefijo, n): 

            if permutacion[i] - ult_ord == 1: 
                inversiones.append((prefijo, i))
                permutacion = permutacion[0:prefijo] + permutacion[prefijo:i+1][::-1] + permutacion[i+1:]

                prefijo = CalculaPrefijo(permutacion)
    return(inversiones)




################################################################################################
############################################ main ##############################################
################################################################################################

def main():
    print("Módulo 'PracticasAlgoritmos'.")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
