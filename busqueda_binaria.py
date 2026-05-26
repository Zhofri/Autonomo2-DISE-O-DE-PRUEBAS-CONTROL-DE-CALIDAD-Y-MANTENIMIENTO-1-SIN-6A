def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Parámetros:
    lista (list): Una lista de elementos ordenados de menor a mayor.
    objetivo: El elemento que se desea buscar en la lista.

    Retorna:
    int: El índice del objetivo en la lista si se encuentra, o -1 si no está presente.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1
