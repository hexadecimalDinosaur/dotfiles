#!/bin/bash

#dig +short myip.opendns.com @resolver1.opendns.com 2> /dev/null
echo $(curl -s https://ipinfo.io/ip 2> /dev/null)
