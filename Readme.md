# Prueba PNN
### Prueba de aplicación Django Rest Framework.

Este proyecto es rudimentario y básico, el cual puede no validar todas las caracteristicas esperadas del mismo.

## Setup Docker
La implementación de este proyecto se realiza en Docker y los archivos `Dockerfile`, `entrypoint.sh` y `start.sh`, implementan toda la lógica de construcción y comunicación.

#### Useful Commands
Todos los comandos deben ser ejecutados desde la ráiz del proyecto.

## Nota: Antes de ejecutar los comandos, copie el archivo `.sample-env` en `.env` en la misma carpeta `docker/` y dilicencie todos los parametros según la configuración deseada.

1. Construya la imagen docker con el tag 'development': `docker build -t dockerapp:development -f docker/Dockerfile .`

2. Inicie los contenedores (Postgis y Django):  `docker-compose -f docker/docker-compose.yml up`

3. Detener todos los contenedores: `docker-compose -f docker/docker-compose.yml down`

4. Detener todos los contenedores y borrar los volumenes: `docker-compose -f docker/docker-compose.yml down -v`

## Detalles del proyecto

1. La aplicación Django es una API REST que consume datos de dos servicios web geográficos, los almacena y realiza intersecciones entre los mismos:
    - La URL `/intersect/area/<idarea>` recupera las intersecciones entre las dos capas de información, filtradas por código del área especial, p.ej. http://localhost:8000/intersect/area/10155.
    - La URL `/intersect/dpto/<coddane>` recupera las intersecciones entre las dos capas de información, filtradas por código DANE de departamentos, p.ej. http://localhost:8000/intersect/dpto/54.


## Componentes utilizados
Para la construcción de este proyecto se utilizaron diferentes fuentes de imagenes y código fuente:
1. Imagen Docker [postgis/postgis](https://hub.docker.com/r/postgis/postgis)
2. Imagen Docker [Python 3.9.9-slim-buster](https://hub.docker.com/_/python)
3. Proyecto para la recuperación de datos REST y almacenamiento en PostGIS *[chupaESRI](https://github.com/johnjreiser/chupaESRI)* (La versión del código a utilizar es la incluida en este proyecto, pues se optimizaron cosas y solucionaron algunos bugs no reportados).
 
