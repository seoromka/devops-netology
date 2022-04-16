#!/usr/bin/env bash

ips=("87.250.250.242" "192.168.5.108" "192.168.5.162" "192.168.5.2")
port=80

while ((1==1))
do
  for ip in ${ips[@]}
  do
    nc -v -z -w 1 -G 1 $ip $port 2&>1 > /dev/null
    if (($? != 0))
    then
      echo $ip > error.txt
      exit 1
    fi
  done
  sleep 1
done
