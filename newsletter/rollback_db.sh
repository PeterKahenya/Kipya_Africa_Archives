#!/usr/bin/env bash

rm -r accounts/migrations
rm -r subscribers/migrations
rm -r dashboard/migrations
rm -r db.sqlite3
./manage.py makemigrations dashboard accounts subscribers
./manage.py migrate
./manage.py createsuperuser --username admin --email peter@kipya-africa.com