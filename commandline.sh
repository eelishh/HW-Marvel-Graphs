#!/bin/bash

echo "What is the most popular pair of heroes (often appearing together in the comics)?"
awk -F, '$1 != $2' hero-network.csv > hero-network-new.csv # remove lines where hero1 == hero2 in hero-network.csv
sort hero-network-new.csv | uniq -c | sort -nr | head -n 1

echo " "

echo "Number of comics per hero:"
cut -d, -f 1 edges.csv | sort | uniq -c | sort -nr| head -n 10

echo " "

echo "The average number of heroes in comics:"
cut -d, -f 1,2 edges.csv | awk -F, '{heroes[$2]++} END{for(i in heroes){t+= heroes[i]; print i, t/length(heroes)}}' | head -n 10