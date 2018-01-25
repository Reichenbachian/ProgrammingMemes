#!/bin/bash
if ! screen -list | grep -q "production"; then
    # run bash script
    source /home/programming_memes/venv/bin/activate;
    screen -S "production" -d -m
    screen -r "production" -X stuff $'source /home/programming_memes/venv/bin/activate; uwsgi --ini Programming_Memes/MemeServer/uwsgi.ini\n'
fi
