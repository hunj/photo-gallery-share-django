#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --no-input
python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn core.wsgi:application --bind 0.0.0.0:8001 --reload
