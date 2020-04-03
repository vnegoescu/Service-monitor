#!/bin/bash

# stop all containers
docker container stop $(docker container ls -q)

# # remove all stopped containers
docker rm $(docker ps -a -q)

docker system prune

# # remove all images
docker rmi $(docker images -a -q)
