# Proyecto Individual | Data 06
# Diego Morales @diegomoos

![image](https://user-images.githubusercontent.com/108296379/182138583-9011699a-f009-4454-885e-80dca182b6c8.png)


## Funcionamiento
Para usar la API localmente necesitaremos clonar el repositorio y instalar los requirements necesarios. Luego ejecutamos el siguiente comando

```bash
uvicorn main:app
```

De esta forma ya se podrá realizar las querys de forma local.

## Respuestas

Las respuestas de las consultas al **API** devuelven un string con el resultado:

```python
'La palabra love se repite 198 veces en la plataforma netflix'
```

## Querys Disponibles

`/get_word_count/`: Listado de todos los años de los que se tiene registro, con la cantidad de carreras por año.

`/get_score_count/`: Listado ordenado con mayor cantidad de carreras por año, en un top según el número indicado.

`/get_second_score/`: Pilotos y la cantidad de veces que consiguieron un primer puesto. Ordenado por cantidad de forma descendente.

`/get_longest/`: Top de pilotos y la cantidad de veces que consiguieron un primer puesto.

`/get_rating_count/`: Nombre de circuitos con cantidad de carreras que se corrieron en él. Ordenado de más carreras a menos.

## Ejemplos

https://2zbw58.deta.dev/get_word_count/?keyword=love&platform=netflix

https://2zbw58.deta.dev/get_score_count/?platform=netflix&score=85&year=2010

https://2zbw58.deta.dev/get_second_score/?platform=amazon

https://2zbw58.deta.dev/get_longest/?platform=netflix&duration_type=min&year=2016

https://2zbw58.deta.dev/get_rating_count/?rating=18%2B