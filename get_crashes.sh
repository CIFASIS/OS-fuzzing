#!/bin/sh


if [ $# -ne 2 ]; then
    # TODO: print usage
    echo xxx
    exit 1
fi

OUTPUTERR=$1.err
OUTPUT=$1.out

printf "" > $OUTPUTERR
#printf "" > $OUTPUT

for testcase in $(ls "$1" | shuf); do
  time --quiet -f "$testcase\t%E\t%x" vdp "$1/$testcase" "$2" 2>> $OUTPUTERR > /dev/null #$OUTPUT
done

