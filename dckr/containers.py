import json
from prettytable import PrettyTable
import colorize
import utility
import sys

def HandleContainer(client):
    containers = client.containers.list(all=True)

    if sys.argv[2].lower() == 'search' or sys.argv[2].lower() == 's':
        if len(sys.argv) < 4:
            print('You need to provide a search term for search to work')
            return
        searchterm = sys.argv[3]
        foundcontainers = []
        for c in containers:
            if searchterm in c.attrs['Id'] or searchterm in c.attrs['Name'] or searchterm in c.attrs['Config']['Image']:
                foundcontainers.append(c)
        print(f'Total {colorize.colorizeNumber(len(foundcontainers))} container(s) found matching search.')
        printContainers(foundcontainers)
        return

    if sys.argv[2].lower() == 'ls':
        print(f'Total {colorize.colorizeNumber(len(containers))} container(s) found.')
        printContainers(containers)
        return

    if sys.argv[2].lower() == 'clean':
        choice = input(f'Total {colorize.colorizeNumber(len(containers))} container(s) will be removed. Proceed (y/n)? ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            # remove logic
            print(f'All container(s) removed')
        else:
            print(f'Container remove aborted')

def printContainers(containers):
    t = PrettyTable(['ID','Name','Image','Status','Ports'])
    for c in containers:
        t.add_row([c.attrs['Id'][:12], utility.ParseName(c.attrs['Name']), c.attrs['Config']['Image'], colorize.colorizeStatus(c.attrs['State']['Status']), utility.ParsePort(c.attrs['HostConfig']['PortBindings'])])
    print(t)
