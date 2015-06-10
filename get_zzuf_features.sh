#!/bin/sh


if [ $# -ne 1 ]; then
    # TODO: print usage
    echo xxx
    exit 1
fi


# crashes

OUTPUT=$1.1.csv
printf "" > $OUTPUT

echo "crashes"

for testcase in $(cat $1 | grep _usr_bin | grep -v "0$" | cut -f 1 | shuf); do
  echo $testcase
  fextractor --timeout 3 --mclass 1 --dynamic "zzuf_testcases/$testcase" >> $OUTPUT
done

# non-crashes

OUTPUT=$1.0.csv
printf "" > $OUTPUT

echo "non-crashes"

for testcase in $(cat $1 | grep _usr_bin | grep "0$" | cut -f 1 | shuf); do
  echo $testcase
  fextractor --timeout 3 --mclass 0 --dynamic "zzuf_testcases/$testcase" >> $OUTPUT
done

