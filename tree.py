#!/usr/bin/python3

from math import ceil
from random import choice
from sys import stdout, argv, exit as sys_exit
from os import system

write = lambda x: stdout.write(x)

clear = lambda: system('clear')

symbols = ["#", "$", "%", "&"]
colors = ['\033[1;32m', '\033[1;36m', '\033[1;34m', '\033[1;33m']
tail = False

try:
    arguments = {
        'tail': False,
        'length': 41
    }

    for index in range(1, len(argv)):
        arg = str(argv[index]).strip()
        if arg == "--tail":
            arguments['tail'] = True
        if "--length" in arg:
            if "=" not in arg:
                if argv[index + 1].isnumeric():
                    arguments['length'] = int(argv[index + 1])
                else:
                    write('[Error]' + '\033[1;31m' + 'Invalid length' + '\033[0m\n')
                    sys_exit(1)
                    exit(1)
            else:
                write('[Error]' + '\033[1;31m' + 'Invalid length' + '\033[0m\n')
                sys_exit(1)
                exit(1)
except Exception as e:
    write('[Error]' + '\033[1;31m' + e + '\033[0m')
    sys_exit(1)
    exit(1)
    arguments['length'] = 41


def print_tree():
    width_current_line = 1
    i = ceil(arguments['length'] / 2) - width_current_line

    while i > 0:
        for a in range(i):
            write(' ')
        for a in range(width_current_line * 2):
            write(choice(colors)+choice(symbols))
        width_current_line += 1
        i -= 1
        write('\n')

if arguments['tail']:
    from time import sleep
    while True:
        try:
            clear()
            print_tree()
            sleep(0.2)
        except KeyboardInterrupt:
            write('\n')
            sys_exit(0)
            exit(0)
else:
    print_tree()
