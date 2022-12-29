#!/bin/sh
cut -d, -f 1 edges.csv | sort | uniq -c | sort -nr| head -n 10


cut -d, -f 1,2 edges.csv | awk -F, '{heroes[$2]++} END{for(i in heroes){t+= heroes[i]; print i, t/length(heroes)}}' | head -n 10
