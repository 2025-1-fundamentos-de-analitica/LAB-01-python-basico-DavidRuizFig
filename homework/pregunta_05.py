"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            
            letra = columns[0]
            valor = int(columns[1])
            
            if letra not in valores_letra:
                valores_letra[letra] = [valor]
            else:
                valores_letra[letra].append(valor)
        
        result =[]
        for letra, valores in valores_letra.items():
            maximo = max(valores)
            minimo = min(valores)
            result.append((letra, maximo, minimo))
        
        result.sort()
        
        return result