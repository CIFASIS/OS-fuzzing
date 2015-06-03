#!/bin/sh

#printf "" > crashes.csv

if [ $# -ne 2 ]; then
    # TODO: print usage
    echo xxx
    exit 1
fi

for testcase in $(ls "$1" | shuf); do
  time --quiet -f "$testcase\t%E\t%x" vdp "$1/$testcase" --check-open-files "$2" #>> crashes.csv
done

