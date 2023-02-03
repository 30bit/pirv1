#!/usr/bin/env bash

cmake CMakeLists.txt
make

printf '' > output.txt

for n in 450
do
    echo $n 5 >> output.txt
    for r in 1 25 50 75 150
    do
        echo "Running with flags - n $n -m $m -r $r"
        ./lab1 -n $n -m $n -r $r
        less output.txt
    done
done