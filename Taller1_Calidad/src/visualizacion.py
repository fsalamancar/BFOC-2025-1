
def visualizar_calidad(ruta_archivo):
    """
    Visualiza la calidad de los datos por secuencias segun la posicion.
    Genera un grafico de dispersion por cada posicion vs la calidad de los datos.
    
    Args:
     (String) ruta del archivo de texto .fasta con datos de calidad .
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt


    #Leer archivo de texto Fastq
    with open(ruta_archivo) as f:
        lines = [line.strip() for line in f]
    
    #Extraer secuencia y calidad
    tabla = []
    for i in range(0, len(lines), 4):
        id_sequencia = lines[i][1:] #para quitar el @
        secuencia = lines[i+1]
        calidad = lines[i+3]
        tabla.append((id_sequencia, secuencia, calidad))
        
    #Crear el df
    df = pd.DataFrame(tabla, columns=['id_sequencia', 'secuencia', 'calidad'])
    
    #poner el nombre de la secuencia como el id
    df.set_index("id_sequencia", inplace=True)
    
    # Expandir cada carácter de la secuencia y calidad en columnas separadas
    secuencia_expandida = df['secuencia'].apply(lambda x: pd.Series(list(x)))
    calidad_expandida = df['calidad'].apply(lambda x: pd.Series(list(x)))

    # Renombrar columnas para claridad
    secuencia_expandida.columns = [f"Base_{i+1}" for i in secuencia_expandida.columns]
    calidad_expandida.columns = [f"Calidad_{i+1}" for i in calidad_expandida.columns]

    # Concatenar ambos DataFrames horizontalmente
    df_expandido = pd.concat([secuencia_expandida, calidad_expandida], axis=1)
    df_expandido.index = df.index  # Mantener el mismo índice
    
    # Convertir los nas a 0
    df_expandido = df_expandido.fillna(0)

    #Convertir todo a strings
    df_expandido = df_expandido.astype(str)

    #hacer copia de la tabla
    df_expandido_copia = df_expandido.copy()

    # Identificar columnas de calidad
    cols_calidad = [col for col in df_expandido_copia.columns if col.startswith('Calidad_')]

    # Convertir cada casilla de calidad a su valor ASCII
    df_expandido_copia[cols_calidad] = df_expandido_copia[cols_calidad].applymap(
     lambda x: ord(x) if isinstance(x, str) and len(x) == 1 else np.nan
    )
    
    #pasar a int las columnas de calidad
    df_expandido_copia[cols_calidad] = df_expandido_copia[cols_calidad].astype(int)
    #restar 33 a cada valor de calidad
    df_expandido_copia[cols_calidad] = df_expandido_copia[cols_calidad] - 33

    #Calcular la calidad promedio
    # Promedio de calidad por posición (columna)
    promedio_por_posicion = df_expandido_copia[cols_calidad].mean(axis=0)
    
    #calcular la desviacion estandar 
    desviacion_por_posicion = df_expandido_copia[cols_calidad].std(axis=0)
    
    
    #Graficar la calidad promedio con desviacion estandar vs posicion
    plt.figure(figsize=(12, 6))
    plt.errorbar(range(1, len(promedio_por_posicion) + 1), promedio_por_posicion, yerr=desviacion_por_posicion, fmt='o', color='black', ecolor='gray', elinewidth=3, capsize=0)
    plt.title('Calidad promedio de la secuencia por posición')
    plt.xlabel('Posición de la base')
    plt.ylabel('Calidad promedio')
    plt.xticks(range(1, len(promedio_por_posicion) + 1))
    plt.grid()
    plt.show()