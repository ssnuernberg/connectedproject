#!/usr/bin/env bash
rm -fr connectedapp/__pycache__
rm -fr connectedapp/migrations/__pycache__
rm -f connectedapp/migrations/0001_initial.py
rm -fr connectedapp/tests/__pycache__
rm -fr connectedproject/__pycache__
rm -f db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata roles
python manage.py loaddata users
python manage.py loaddata statuses
python manage.py loaddata courses
python manage.py loaddata feedbacks
