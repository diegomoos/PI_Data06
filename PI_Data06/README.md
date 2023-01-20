# Proyecto Individual | Data 06
# Diego Morales @diegomoos

![image](https://user-images.githubusercontent.com/108296379/182138583-9011699a-f009-4454-885e-80dca182b6c8.png)


## Funcionamiento
Para usar la API localmente necesitaremos clonar el repositorio y instalar los requirements necesarios. Luego ejecutamos el siguiente comando

```bash
uvicorn main:app
```

De esta forma ya se podrá realizar las querys de forma local.

[API en Deta](https://2zbw58.deta.dev/docs#/)

## Respuestas

Las respuestas de las consultas al **API** devuelven un string con el resultado:

```python
'La palabra love se repite 198 veces en la plataforma netflix'
```

## Querys Disponibles

`/get_word_count/`: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.

`/get_score_count/`: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

`/get_second_score/`: La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

`/get_longest/`: Película que más duró según año, plataforma y tipo de duración.

`/get_rating_count/`: Cantidad de series y películas por rating.

## Ejemplos

https://2zbw58.deta.dev/get_word_count/?keyword=love&platform=netflix

https://2zbw58.deta.dev/get_score_count/?platform=netflix&score=85&year=2010

https://2zbw58.deta.dev/get_second_score/?platform=amazon

https://2zbw58.deta.dev/get_longest/?platform=netflix&duration_type=min&year=2016

https://2zbw58.deta.dev/get_rating_count/?rating=18%2B
