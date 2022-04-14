import PracticasAlgoritmos as pa

# Entradas ejemplo:
ejemplos = [[1, 2, 3, 6, 4, 5],
            [6, 1, 2, 3, 4, 5],
            [3, 4, 2, 1, 5, 6, 7, 10, 9, 8]]


for i, ejemplo in enumerate(ejemplos):
    print("### Ejemplo {}:\nEntrada: permutacionInicial = {}".format(i+1, ejemplo))
    try:
        X = pa.OrdenacionInversionSimple(ejemplo)
        print("Salida: {}\n".format(X))
    except Exception as e:
        print("Salida: Error: {}\n".format(e))