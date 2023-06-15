
## docker-commands

* Add the <UserName> to the docker group so you can execute Docker commands without using sudo
```bash
sudo usermod -a -G docker <USER-NAME>
```

* see all running containers
```bash
docker ps
```

* stop/kill running container
```bash
docker stop/kill <CONTAINER-ID>
```
* start a stopped container
```bash
docker start <CONTAINER-ID>
```
* all container running/stopped
```bash
docker ps -a 
```
* build a docker image
```bash
docker build .
```

```bash
docker build -t anubhaw/redis:latest .
```
* run a shell within a docker container  using (-it)
```bash
docker run -it alpine sh
```

```bash
docker exec -it <CONTAINER-ID> /bin/bash 
```

```bash
docker exec -it <CONTAINER-ID> /bin/sh
```

* take the systemfile snapshot of the container with <CONTAINER-ID> and will execute with the startup command as provided i.e-  CMD "redis-server"
```bash
docker commit -c 'CMD "redis-server"' 
```
* host port allocation for two containers running on same ports.
```bash
docker run -p6000:6379 redis:4.0
```
* docker logs 
```bash
docker logs <containerID/Name> 
```
* renaming a docker container
```bash
docker run --name <Container New Name> <IMAGE>
```
* for running container in detachable mode
```bash
docker run -d <IMAGE>
```
* docker Networks
```bash
docker network create <NETWORK-NAME>
```
* delete/remove an image
```bash
docker image rm <IMAGE/CONTAINER-ID>
```
* remove a docker container
```bash
docker rm <CONTAINER-ID/NAME>
```
* remove a docker image
```bash
docker rmi <IMAGE-NAME>
```
* copy a file from docker container to local machine
```bash
docker cp <container_id_or_name>:<source_path> <local_destination_path>
```


