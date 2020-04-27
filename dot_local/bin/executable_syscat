#!/bin/bash
# syscat
# a info script thrown together
# created by UserBlackBox based off of Nero's version (ssh-dw)

f=3 b=4
for j in f b; do
  for i in {0..7}; do
    printf -v $j$i %b "\e[${!j}${i}m"
  done
done

B='[1m'
R='[0m'
I='[7m'

USR=$(whoami)
HOS=$(hostname)

temp=$(cat /etc/os-release | grep NAME=\"*\" -m 1)
temp=${temp//\"}
temp=${temp//\//}
temp=${temp:5:100}
OS1=$(echo $temp) 
temp=$(cat /etc/os-release | grep VERSION=\"*\" -m 1)
temp=${temp//\"}
temp=${temp//\//}
temp=${temp:8:100}
OS2=$(echo $temp)
KRN=$(uname -rms)
KRN=${KRN:6:100}
temp=$(cat /proc/cpuinfo | grep "model name" -m 1)
CPU=${temp:13:100}
UPT=$(uptime | awk -F, '{sub(".*up ",x,$1);print $1}' | sed -e 's/^[ \t]*//')

PKG=$(apt list --upgradable 2>/dev/null | wc -l)
TX1=UPTIME:
TX2=UPDATES:
TX3=OS:
TX4=KERNEL:
TX5=CPU:
TX6=packages
TX7=DESKTOP:
TX8=MODEL:
TX9=TERM:
TX10=SHELL:
TX11=HOME:
TERMEMULATOR=$(ps -o comm= -p "$(($(ps -o ppid= -p "$(($(ps -o sid= -p "$$")))")))")
MOD=$(cat /sys/devices/virtual/dmi/id/product_name)

if [ "$1" = "-c" ] || [ "$1" = "-color" ]
then

cat << EOF

$f6           ──────▄▀▄─────▄▀▄
$f6           ─────▄█░░▀▀▀▀▀░░█▄
$f6           ─▄▄──█░░░░░░░░░░░█──▄▄
$f6           █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█$R
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
$f1   ▀▀▀▀▀$f2 ▀▀▀▀▀$f3 ▀▀▀▀▀$f4 ▀▀▀▀▀$f5 ▀▀▀▀▀$f6 ▀▀▀▀▀$f7 ▀▀▀▀▀ 
$B$f1   ▀▀▀▀▀$f2 ▀▀▀▀▀$f3 ▀▀▀▀▀$f4 ▀▀▀▀▀$f5 ▀▀▀▀▀$f6 ▀▀▀▀▀$f7 ▀▀▀▀▀$R
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

EOF

else 

cat << EOF

$f6                ──────▄▀▄─────▄▀▄
$f6                ─────▄█░░▀▀▀▀▀░░█▄
$f6                ─▄▄──█░░░░░░░░░░░█──▄▄
$f6                █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█$R
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        $f6$USR@$HOS
        $f1$TX3 $f4$OS1 $OS2
        $f1$TX4 $f4$KRN
	$f1$TX8 $f4$MOD
        $f1$TX5 $f4$CPU
        $f1$TX1 $f4$UPT 
        $f1$TX2 $f4$PKG $TX6
	$f1$TX11 $f4$HOME
	$f1$TX7 $f4$DESKTOP_SESSION
	$f1$TX10 $f4$SHELL
	$f1$TX9 $f4$TERMEMULATOR$R
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

EOF
fi
