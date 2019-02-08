#!/bin/bash

top -b -n 1 -o %CPU | tail -n -10  #display top 10 CPU consumers on console

for i in {1..10}
do
    # create directory and write to file
    mkdir "dir$i"
    top -b -n 1 -o %CPU | tail -n -10 | awk "NR==$(($i + 1))" > dir$i/file$i
done

