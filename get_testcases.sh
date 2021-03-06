#!/bin/sh

printf "" > testcases.csv

for bin in $(ls $@ | shuf); do
  binp="$(which $bin)"
  if [ "$(file $binp | grep 'ELF 32-bit LSB')" ] ; then
    echo $binp
    manfuzzer $binp -n 10 --seeds ../seeds >> testcases.csv
  fi
done

tcreator testcases.csv zzuf_testcases
