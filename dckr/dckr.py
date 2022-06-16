import docker
import sys
import help
import containers, images, volumes

def main():
    myClient = docker.from_env()

    if sys.argv[1].lower() == 'container' or sys.argv[1].lower() == 'c':
        containers.HandleContainer(myClient)
    if sys.argv[1].lower() == 'image' or sys.argv[1].lower() == 'i':
        images.HandleImage(myClient)
    if sys.argv[1].lower() == 'volume' or sys.argv[1].lower() == 'v':
        volumes.HandleVolumes(myClient)
    if sys.argv[1].lower() == 'help':
        help.PrintHelp()

if __name__ == "__main__":
    main()