#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
    python << END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${POSTGRES_DBNAME}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASS}",
        host="${PG_HOST}",
        port="${PG_PORT}",
    )
except OperationalError:
    sys.exit(-1)
END
}

until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 5
done
>&2 echo "PostgreSQL is available"

python3 load_data/chupaESRI.py ${URL_LAYER1} "host=${PG_HOST} dbname=${POSTGRES_DBNAME} user=${POSTGRES_USER} password=${POSTGRES_PASS}" "public.${NAME_LAYER1}"

python3 load_data/chupaESRI.py ${URL_LAYER2} "host=${PG_HOST} dbname=${POSTGRES_DBNAME} user=${POSTGRES_USER} password=${POSTGRES_PASS}" "public.${NAME_LAYER2}"

geometry_ready() {
    python << END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:

    print("Clean Geometry Layers")

    with connect(dbname="${POSTGRES_DBNAME}", user="${POSTGRES_USER}", password="${POSTGRES_PASS}", host="${PG_HOST}", port="${PG_PORT}") as conn:
        conn.autocommit = True
        with conn.cursor() as curs:
            curs.execute("UPDATE public.${NAME_LAYER1} SET shape=ST_Multi(ST_CollectionExtract(ST_MakeValid(shape), 3)) WHERE NOT ST_IsValid(shape)")
            curs.execute("UPDATE public.${NAME_LAYER2} SET shape=ST_Multi(ST_CollectionExtract(ST_MakeValid(shape), 3)) WHERE NOT ST_IsValid(shape)")            

except OperationalError:
    sys.exit(-1)
END
}

until geometry_ready; do
  >&2 echo "Waiting for Geometry to become available..."
  sleep 5
done
>&2 echo "Geometry is available"

python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
