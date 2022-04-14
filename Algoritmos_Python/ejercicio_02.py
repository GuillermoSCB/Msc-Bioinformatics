import PracticasAlgoritmos as pa

# Entradas ejemplo:
ejemplos = [[7, [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]],
            [3, [2, 3, 5]]]


for i, ejemplo in enumerate(ejemplos):
    n = ejemplo[0]
    L = ejemplo[1]
    print("### Ejemplo {}:\nEntrada: n = {}, L = {}".format(i+1, n, L))
    try:
        X = pa.MapaRestriccionesBusquedaExhaustiva(n, L)
        print("Salida: {}\n".format(X))
    except Exception as e:
        print("Salida: Error: {}\n".format(e))