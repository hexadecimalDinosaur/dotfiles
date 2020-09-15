#!/bin/bash
result=$(ps -C redshift | grep -o redshift)
if [[ $result == "redshift" ]]
then
redshift -x && killall redshift && notify-send "Screen Temperature Reset" -t 2000 
else
redshift  -t 3000:3000 &
notify-send "Redshift on" -t 2000
fi
