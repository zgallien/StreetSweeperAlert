#!/bin/bash

# Script to run streetsweeper.py
# Made for ease of use with cron job

# get path to script and cd to dir
SCRIPTPATH=/home/pi/python_projects/street_sweeper
echo "cwd: $SCRIPTPATH"
cd $SCRIPTPATH

# check for virtualenv 
if [ -d "venv" ]; then
    echo "[>>] virtualenv found"
else
    echo "[!!] could not find virtualenv"
    exit 1
fi

# activate virtualenv
echo "Activating virtualenv"
echo "Path pre-activate: $PATH"
path_to_activate=$SCRIPTPATH/venv/bin/activate
. $path_to_activate
echo "Path post-activate: $PATH"

if [ $? != 0 ]; then
    echo "[!!] Failed to activate virtualenv"
    exit 1
else
    echo "[>>] Activated"
fi

# run script
echo "[>>] Running streetsweeper.py"
python3 streetsweeper.py

if [ $? != 0 ]; then
    echo "[!!] Failed"
    exit 1
else
    echo "[>>] Success!"
fi

