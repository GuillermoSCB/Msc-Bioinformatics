import PracticasAlgoritmos as pa

# Entradas ejemplo:
ejemplos = [[0, 6, 7, 8, 9, 11, 12],
            [0, 4, 5]]


for i, ejemplo in enumerate(ejemplos):
    print("### Ejemplo {}:\nEntrada: posCortes = {}".format(i+1, ejemplo))
    try:
        DX = pa.CalculaDX(ejemplo)
        print("Salida: {}\n".format(DX))
    except Exception as e:
        print("Salida: Error: {}\n".format(e))