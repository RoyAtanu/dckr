# pull images
docker pull busybox
docker pull hello-world
docker pull alpine

# start containers
docker run -d busybox
docker run -d hello-world
docker run -d alpine

# create volumes
docker volume create --driver local volume1
docker volume create --driver local volume2
docker volume create --driver local volume3