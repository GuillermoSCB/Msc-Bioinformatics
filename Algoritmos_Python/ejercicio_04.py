import PracticasAlgoritmos as pa

# Entradas ejemplo:
ejemplos = [[pa.MapaRestriccionesBusquedaExhaustivaOptimizada, [3, [2, 998, 1000]] ],
            [pa.MapaRestriccionesBusquedaExhaustiva, [3, [2, 998, 1000]]]]


for i, ejemplo in enumerate(ejemplos):
    func = ejemplo[0]
    args = ejemplo[1]
    print("### Ejemplo {}:\nEntrada: func = {}, args = {}".format(i+1, func, args))
    try:
        tiempo = pa.TiempoEjecucion(func, *args)
        print("Salida: {}\n".format(tiempo))
    except Exception as e:
        print("Salida: Error: {}\n".format(e))