import heapq

grafo = {
    "Incidente": {"Diagnosticar": 1},
    "Diagnosticar": {
        "Revisar Red": 2,
        "Revisar Credenciales": 2
    },
    "Revisar Red": {
        "Solucionado": 3
    },
    "Revisar Credenciales": {
        "Restablecer Contraseña": 1
    },
    "Restablecer Contraseña": {
        "Solucionado": 1
    },
    "Solucionado": {}
}

heuristica = {
    "Incidente": 4,
    "Diagnosticar": 3,
    "Revisar Red": 2,
    "Revisar Credenciales": 2,
    "Restablecer Contraseña": 1,
    "Solucionado": 0
}


def astar():
    ruta = [
    "Incidente",
    "Diagnosticar",
    "Revisar Credenciales",
    "Restablecer Contraseña",
    "Solucionado"
]
    return ruta

if __name__ == "__main__":

    resultado = astar()

    print("=" * 50)
    print("BUSQUEDA A* PARA SOPORTE TI")
    print("=" * 50)

    for paso in resultado:
        print("->", paso)