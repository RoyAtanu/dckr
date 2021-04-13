from termcolor import colored
import sys

def colorizeStatus(status):
    if status.lower() == 'running':
        return colored(status, 'green')
    elif status.lower() == 'exited':
        return colored(status, 'red')
    else:
        return colored(status, 'yellow')

def colorizeNumber(number):
    return colored(number, 'blue')