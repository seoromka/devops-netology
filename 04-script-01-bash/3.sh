#!/usr/bin/env bash

ips=("87.250.250.242" "192.168.5.108" "192.168.5.162" "192.168.5.2")
port=80
declare -i count

for ip in ${ips[@]}
do
  count=5
  while (($count > 0))
  do
    nc -v -z -w 1 -G 1 $ip $port 2&>1 > /dev/null
    if (($? != 0))
    then
      echo "$ip:$port - недоступен" >> log.txt
    else
      echo "$ip:$port - доступен" >> log.txt
    fi

    count=$count-1
  done
done
