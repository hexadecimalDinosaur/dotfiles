#!/bin/bash
windscribe status | grep DISCONNECTED > /dev/null
if [ $? -eq 0 ]; then
	windscribe connect
else
	windscribe disconnect
fi
