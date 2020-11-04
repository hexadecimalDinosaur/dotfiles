#!/bin/bash
result=$(ps -C redshift | grep -o redshift)
if [[ $result == "redshift" ]]
then
redshift -x && killall redshift && notify-send "Screen Temperature Reset" -t 2000 
else
redshift -l 43.4:79.2  &
notify-send "Redshift on" -t 2000
fi
