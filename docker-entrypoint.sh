#!/bin/bash
python manage.py collectstatic --no-input --clear

echo "Prep logs folder"
mkdir -p /opt/logs
touch /opt/logs/gunicorn.log
touch /opt/logs/access.log
tail -n 0 -f /opt/logs/*.log &

echo "Starting Gunicorn."
exec gunicorn svesim.wsgi:application \
    --name svesim \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 \
    --log-level=info \
    --log-file=/opt/logs/gunicorn.log \
    --access-logfile=/opt/logs/access.log \
    "$@"