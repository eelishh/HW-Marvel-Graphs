#!/bin/bash

echo "What is the most popular pair of heroes (often appearing together in the comics)?"
awk -F, '$1 != $2' hero-network.csv | sort  | uniq -c | sort -nr | head -n 1

echo " "

echo "Number of comics per hero:"
cut -d, -f 1 edges.csv | sort | uniq -c | sort -nr| head -n 10

echo " "

echo "The average number of heroes in comics is:"
awk -F',' '{heroes_per_comic[$2]++; total_heroes++} END{ mean=total_heroes/length(heroes_per_comic); print mean}' edges.csv