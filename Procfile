web: gunicorn anticovid.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate