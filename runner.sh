#!/bin/bash
# shellcheck disable=SC2164
cd client
npm start &
P1=$!
# shellcheck disable=SC2103
cd ..
python3 server/manage.py runserver 0.0.0.0:8000 &
P2=$!
wait $P1 $P2