#!/bin/sh

echo "Running migrations..."
python bloom/manage.py migrate

echo "Starting server..."
exec "$@"

