"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            
            letra_col1 = columns[0]
            elementos_col5 = columns[4].split(',') if len(columns) > 4 else []
            
            suma_valores = 0
            for elemento in elementos_col5:
                _, valor = elemento.split(':')
                suma_valores += int(valor)
            
            if letra_col1 in sumas_por_letra:
                sumas_por_letra[letra_col1] += suma_valores
            else:
                sumas_por_letra[letra_col1] = suma_valores
    
    return sumas_por_letra