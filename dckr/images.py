from prettytable import PrettyTable
import colorize
import utility
import sys

def HandleImage(client):
    images = client.images.list()

    if sys.argv[2].lower() == 'search' or sys.argv[2].lower() == 's':
        if len(sys.argv) < 4:
            print('You need to provide a search term for search to work')
            return
        searchterm = sys.argv[3]
        foundimages = []
        for i in images:
            if searchterm in i.attrs['Id'] or searchterm in utility.ParseRepository(i.attrs['RepoDigests'], i.attrs['RepoTags']):
                foundimages.append(i)
        print(f'Total {colorize.colorizeNumber(len(foundimages))} container(s) found matching search.')
        printImages(foundimages)
        return

    if sys.argv[2].lower() == 'ls':
        print(f'Total {colorize.colorizeNumber(len(images))} image(s) found.')
        printImages(images)
    
    if sys.argv[2].lower() == 'clean':
        choice = input(f'Total {colorize.colorizeNumber(len(images))} will be removed. Proceed (y/n)? ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            for i in images:
                client.images.remove(i.attrs['Id'][7:19], force=True)
            print(f'All images removed')
        else:
            print(f'Image remove aborted')

def printImages(images):
    t = PrettyTable(['ID','Repository','Tag','Size'])
    for i in images:
        t.add_row([i.attrs['Id'][7:19], utility.ParseRepository(i.attrs['RepoDigests'], i.attrs['RepoTags']), utility.ParseTag(i.attrs['RepoTags']), utility.ParseSize(i.attrs['Size'])])
    print(t)