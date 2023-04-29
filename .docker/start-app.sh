#!/bin/bash
cp ./src/.env.example ./src/.env
pip install -r requirements.txt
tail -f /dev/null