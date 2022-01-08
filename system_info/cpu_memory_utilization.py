#!/usr/bin/env python3

import os
import psutil

def main():
    cpu_command = '''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' '''
    cpu_percentage = str(round(float(os.popen(cpu_command).readline()), 2))
    memory_percentage = psutil.virtual_memory().percent
    print(' CPU       RAM')
    print(cpu_percentage+'%', '  ', str(memory_percentage)+'%')


if __name__ == '__main__':
    main()
