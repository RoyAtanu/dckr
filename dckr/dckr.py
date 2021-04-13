import docker
import sys
import containers
import images

def main():
    myClient = docker.DockerClient(base_url='unix://var/run/docker.sock')

    if sys.argv[1].lower() == 'container' or sys.argv[1].lower() == 'c':
        containers.HandleContainer(myClient)
    if sys.argv[1].lower() == 'image' or sys.argv[1].lower() == 'i':
        images.HandleImage(myClient)

if __name__ == "__main__":
    main()