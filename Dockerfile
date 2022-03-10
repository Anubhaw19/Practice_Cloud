#step1- specify base Image
FROM alpine

#step2- Download and install dependencies
RUN apk add --update redis

#step3- steup the startup command 
CMD ["redis-server"]



#----some-docker-commands--------------------------------------

#see all running containers
#$ docker ps 

#stop/kill running container
#$ docker stop/kill <CONTAINER-ID>

#start a stopped container
#$ docker start <CONTAINER-ID>
#docker run will create a new container whereas docker start will start a stopped container

# all container running/stopped
#$ docker ps -a 

#$ docker build .
#$ docker build -t anubhaw/redis:latest .

# run a shell within a docker container  using (-it)
#$ docker run -it alpine sh
# using the above command we a run a shell within a linux alpine image & execute commands
or
#$ docker exec -it <CONTAINER-ID> /bin/bash 
or
#$ docker exec -it <CONTAINER-ID> /bin/sh

#$ docker commit -c 'CMD "redis-server"' 
# above command take the systemfile snapshot of the container with <CONTAINER-ID> and will execute with the startup command as provided i.e-  CMD "redis-server"

# host port allocation for two containers running on same ports.
#$ docker run -p6000:6379 redis:4.0

#$ docker logs <containerID/Name>

# renaming a docker container
#$ docker run --name <Container New Name> <IMAGE>

# for running container in detachable mode
# $ docker run -d <IMAGE>

#docker Networks
#$ docker network create <NETWORK-NAME>

# delete/remove an image
#$ docker image rm <IMAGE/CONTAINER-ID>
