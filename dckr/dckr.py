import docker
import sys
import containers
import images

def main():
    myClient = docker.from_env()

    if sys.argv[1].lower() == 'container' or sys.argv[1].lower() == 'c':
        containers.HandleContainer(myClient)
    if sys.argv[1].lower() == 'image' or sys.argv[1].lower() == 'i':
        images.HandleImage(myClient)

if __name__ == "__main__":
    main()