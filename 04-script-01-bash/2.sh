#!/usr/bin/env bash

while ((1==1))
do
	curl -I https://localhost:4757
	if (($? != 0))
	then
		date >> curl.log
	else
	  echo "Сервис доступен!"
	  break
	fi

	sleep 5
done
