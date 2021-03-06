import sys
import colorize
from prettytable import PrettyTable

def HandleVolumes(client):
    volumes = client.volumes.list()

    if sys.argv[2].lower() == 'search' or sys.argv[2].lower() == 's':
        if len(sys.argv) < 4:
            print('You need to provide a search term for search to work')
            return
        searchterm = sys.argv[3]
        foundvolumes = []
        for v in volumes:
            if searchterm in v.attrs['Name']:
                foundvolumes.append(v)
        print(f'Total {colorize.colorizeNumber(len(foundvolumes))} container(s) found matching search.')
        printVolumes(foundvolumes)
        return

    if sys.argv[2].lower() == 'ls':
        print(f'Total {colorize.colorizeNumber(len(volumes))} container(s) found.')
        printVolumes(volumes)
        return

    if sys.argv[2].lower() == 'clean':
        choice = input(f'Total {colorize.colorizeNumber(len(volumes))} volume(s) will be removed. Proceed (y/n)? ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            for v in volumes:
                v.remove(force=True)
            print(f'All volume(s) removed')
        else:
            print(f'Volume remove aborted')

def printVolumes(volumes):
    t = PrettyTable(['Name','Driver'])
    for v in volumes:
        t.add_row([v.attrs['Name'], v.attrs['Driver']])
    print(t)