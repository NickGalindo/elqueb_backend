#!/bin/bash

COLOR_OFF='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
BROWN='\033[0;33m'
BLUE='\033[0;34m'

if [ $1 == 'build' ]
then
  printf "${BROWN}Building mongodb container${COLOR_OFF}\n"
  docker run -d -p 27017:27017 --name mongodb -v ./data-vol:/data/db mongo:latest
elif [ $1 == 'start' ]
then
  printf "${GREEN}Starting mongodb${COLOR_OFF}\n"
  docker start mongodb
elif [ $1 == 'stop' ]
then
  printf "${BLUE}Stopping containers${COLOR_OFF}\n"
  docker stop mongodb
elif [ $1 == 'clean' ]
then
  printf "${RED}Cleaning up containers${COLOR_OFF}\n"
  rm -rf data-vol
elif [ $1 == 'purge' ]
then
  printf "${RED}Purging containers and images${COLOR_OFF}\n"
  docker rm mongodb
fi
