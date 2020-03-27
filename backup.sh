#!/bin/bash

source ./backup.config

DATE=`date +"%Y-%m-%d_%H-%M-%S"`

pg_dump -U quack -h localhost -f ~/backups/"backup-$DATE.dump" quack_db

cd ~/backups

NUM=`ls -l | grep "backup" | wc -l`

if [ $NUM -gt $NUM_OF_ROTATIONS ]
then

for (( i==1; i<(($NUM-$NUM_OF_ROTATIONS)); i++ ))
do

rm ./$(ls | grep "backup" | sort | head -n 1)

done
fi


