from fastapi import FastAPI
import pandas as pd

app= FastAPI(title='Proyecto Individual 01 | Data 06',
            description='¡Bienvenidos a mi Proyecto!',
            version='1.0.0')


# Leemos el DataFrame final con pandas, importando el csv

dataframe = pd.read_csv('./Datasets/all_platforms_titles-score.csv')

@app.get("/get_word_count/")

async def get_word_count(keyword:str, platform:str):
    df_gwc = dataframe[['platform','title']].loc[dataframe['platform'] == platform]
    result = df_gwc['title'].str.count(keyword).sum()
    return f'La palabra {keyword} se repite {result} veces en la plataforma {platform}'

@app.get("/get_score_count/")

async def get_score_count(platform:str, score:int, year:int):
    df_gsc = dataframe[['platform','release_year','score']].loc[(dataframe['platform'] == platform) & (dataframe['release_year'] == year) & (dataframe['score'] > score)]
    result_two = df_gsc['platform'].count()
    return f'La cantidad de Peliculas con un score mayor a {score} en {platform} es {result_two}'

@app.get("/get_second_score/")

async def get_second_score(platform:str):
    df_gsecondc = dataframe[['platform','score','title']].loc[dataframe['platform'] == platform]
    df_gsecondc['title-rm-especial_ch'] = df_gsecondc['title'].str.replace('\W', '', regex=True).replace('\d+', '', regex=True)
    second_one = df_gsecondc.sort_values(by=['score','title-rm-especial_ch'], ascending=[False,True]).reset_index()
    result = (second_one['title'][1], second_one['score'][1])
    return f'La Segunda Pelicula con Mayor Score en {platform} es {result[0]} con un puntaje de {result[1]}'

@app.get('/get_longest/')

async def get_longest(platform:str,duration_type:str,year:int):
    df_gt = dataframe[['title','platform','duration_int', 'duration_type','release_year']].loc[(dataframe['platform'] == platform) & (dataframe['release_year'] == year) & (dataframe['duration_type'] == duration_type)]
    longest = df_gt.loc[df_gt['duration_int'] == df_gt['duration_int'].max()]
    result = longest.reset_index()
    title = result['title'][0]
    duration_int = result['duration_int'][0]
    return f'La Pelicula que mas duro en el anio {year} en {platform} fue {title} con {duration_int} {duration_type} de duracion'


@app.get('/get_rating_count/')

async def get_rating_count(rating:str):
    result_grt = dataframe['rating'].loc[dataframe['rating'] == rating].count()
    return f'La Cantidad de Titulos con el Rating {rating} es {result_grt}'