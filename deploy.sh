#!/usr/bin/env bash
python3 -m pip install -r requirements.txt
cd eksiclone
python3 manage.py makemigrations mainsite
python3 manage.py migrate
python3 pre_deploy.py
sudo python3 deploy.py