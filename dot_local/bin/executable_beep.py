#!/usr/bin/python3
import sys

args = sys.argv

if "-h" in args or "--help" in args: # help message
    beep=args[0] # dynamic example message
    print("pybeep - python3 alternative to beep using ALSA")
    print("===============================================")
    print(beep+" [-f N] [-l N] [-d N]")
    print(beep+" [ OPTIONS ] [-n] [ OPTIONS ]")
    print(beep+" [-h] [--help]")
    print("")
    print("Parameters:")
    print("-h, --help   show this help page")
    print("-f N         specify tone frequency where 0<N<20000")
    print("-l N         specify tone duration in milliseconds")
    print("-d N         specify gap duration between tones in milliseconds")
    print("-n           split between multiple tones in one command run")
    print("--verbose    show ALSA messages")
    exit()

if "--verbose" not in args: # hide ALSA error messages
    from ctypes import *
    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    def py_error_handler(filename, line, function, err, fmt):
        pass
    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
else: args.remove("--verbose")

from pysine import sine
import itertools
import time

args = args[1:]

if args == []: # default tone
    sine(440,1)
    exit()

args = [list(g[1]) for g in itertools.groupby(args, key= lambda x: x != '-n') if g[0]] # split by '-n'
freq = 440
duration = 1
gap = 0

for i in range(len(args)):
    freq = 440 # defaults if unspecified
    duration = 1
    gap = 0
    for j in range(len(args[i])):
        if args[i][j] == "-f": # specify frequencies
            try: freq = float(args[i][j+1])
            except:
                print("Invalid argument format\nView help with "+beep[0]+" -h")
                exit()
        if args[i][j] == "-l": # specify durations
            try: duration = float(args[i][j+1])/1000 # convert to seconds
            except:
                print("Invalid argument format\nView help with "+beep[0]+" -h")
                exit()
        if args[i][j] == "-d" or args[i][j] == "-D": # specify gap
            try: gap = int(args[i][j+1])/1000
            except:
                print("Invalid argument format\nView help with "+beep[0]+" -h")
                exit()
    sine(frequency=freq,duration=duration) # play tone
    time.sleep(gap) # gap between tones
exit()
