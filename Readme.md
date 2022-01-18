# Prueba PNN
#### A test Django application with production-level docker setup.

This project is to document production-level Docker setup. Please note that Django application is rudimentary and not fit for production.

## Docker Setup
Detailed documentation of Docker setup can be found in above blog.
It discusses in detail `Dockerfile`, `entrypoint.sh` and `start.sh`

#### Useful Commands
To be run from root of the project.

Note: Before running commands, copy `.sample-env` into `.env` in the same level `dockerapp/docker/` and fill all parameters.
1. Build docker image with tag 'development':
`docker build -t dockerapp:development -f docker/Dockerfile .`

2. Start all containers including essential services(PostgreSQL and Redis):  `docker-compose -f docker/docker-compose.yml up`

3. Stop all containers: `docker-compose -f docker/docker-compose.yml down`

4. Stop all containers and delete volumes: `docker-compose -f docker/docker-compose.yml down -v`

## Django application details
1. The Django application has a api REST linked to url `/intersect/dpto` filter the intersect Layer 1 and 2.


Using `chupaESRI` [https://github.com/johnjreiser/chupaESRI]
 
