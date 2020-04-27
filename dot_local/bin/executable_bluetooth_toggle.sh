#!/bin/bash
rfkill | grep "hci0     blocked" > /dev/null
if [ $? -eq 0 ]; then
	rfkill unblock 1
else
	rfkill block 1
fi
