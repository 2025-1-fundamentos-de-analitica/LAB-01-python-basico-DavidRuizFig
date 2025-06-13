"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.



    """
    conteoclaves = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            
            if len(columns) >= 5:
                kvs = columns[4].split(',')
                
                for kv in kvs:
                    k,_= kv.split(':')
                    
                    if k in conteoclaves:
                        conteoclaves[k] += 1
                    else:
                        conteoclaves[k] = 1
                        
    return conteoclaves
                    