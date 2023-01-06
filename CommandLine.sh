#!/bin/bash

echo "What is the most popular pair of heroes (often appearing together in the comics)?"
awk -F, '$1 != $2' hero-network.csv | sort  | uniq -c | sort -nr | head -n 1

echo " "

echo "Number of comics per hero:"
cut -d, -f 1 edges.csv | sort | uniq -c | sort -nr| head -n 10

echo " "

echo "The average number of heroes in comics:"
awk -F',' '{heroes_per_comic[$1]++; total_heroes++} END{for (comic in heroes_per_comic) num_comics++; mean=total_heroes/num_comics; printf "average number of heroes in comic: %d\n", mean}' edges.csv
