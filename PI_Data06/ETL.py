def etl():    
    # Importamos las librerias necesarias
    import pandas as pd

    # Cargamos los archivos .csv necesarios con la función de pandas 'read_csv'

    df_amazon = pd.read_csv('./Datasets/amazon_prime_titles-score.csv')
    df_disney = pd.read_csv('./Datasets/disney_plus_titles-score.csv')
    df_hulu = pd.read_csv('./Datasets/hulu_titles-score (2).csv')
    df_netflix = pd.read_csv('./Datasets/netflix_titles-score.csv')

    # Agregamos una columna a cada dataframe que identifique la Plataforma

    df_amazon['platform'] = 'amazon'
    df_disney['platform'] = 'disney'
    df_hulu['platform'] = 'hulu'
    df_netflix['platform'] = 'netflix'

    # Creamos una lista con los DataFrames
    dfs_list = [df_amazon, df_disney, df_hulu, df_netflix]

    def id_column(dataframe: pd.DataFrame, letter: str):
        ''' 
        Agrega una nueva columna 'id' al principio del contenido de la columna 'show_id' en un DataFrame
        '''
        dataframe['id'] = letter+dataframe['show_id']

    # Creamos una lista con las letras correspondientes

    letters = ['a', 'd', 'h', 'n']

    # Aplicamos la funcion "id_column" a cada Dataframe

    for i, df in enumerate(dfs_list):
        id_column(df, letters[i])

    # Concatenamos los Dataframes, para que esto funcione todos los dataframe tienen que tener el mismo tipo de columnas

    dataframe = pd.concat([dfs_list[0], dfs_list[1], dfs_list[2], dfs_list[3]])

    # Cambiamos los valores nulos en la columna rating por la letra 'G'

    dataframe['rating'].fillna('G', inplace=True)

    # Transformamos el formato de las fechas en 'AAAA-mm-dd'

    dataframe['date_added'] = dataframe['date_added'].str.strip()
    dataframe['date_added'] = pd.to_datetime(dataframe['date_added'], format='%B %d, %Y')
    dataframe['date_added'] = dataframe['date_added'].dt.strftime('%Y-%m-%d')

    # Cambiamos todos los campos de texto del dataframe en minusculas

    for col in dataframe.select_dtypes(include=['object']):
        dataframe[col] = dataframe[col].str.lower()

    # A travez del metodo 'split' separamos la columna duration en dos, una con el digito y la otra con su unidad

    split = dataframe['duration'].str.split(' ', n=1, expand=True)
    dataframe['duration_int'] = split[0]
    dataframe['duration_type'] = split[1]

    # Cambiamos el tipo de dato de la nueva columna 'duration digit' de object a integer

    dataframe['duration_int'].fillna('0', inplace=True)
    dataframe['duration_int'] = dataframe['duration_int'].astype(int)

    # Estandarizamos la unidad "Season" y "Seasons" por season solamente

    dataframe['duration_type'] = dataframe['duration_type'].str.replace('ns', 'n', regex=False)

    # Finalmente exportamos nuestro DataFrame ya modificado

    dataframe.to_csv('Datasets/all_platforms_titles-score.csv')

etl()
