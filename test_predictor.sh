for seed in $(seq 0 20); do
  python split.py $1 $seed
  vpredictor --out-file data/$seed/zzuf.pklz --train --dynamic data/$seed/train.csv > /dev/null
  vpredictor --test --model data/$seed/zzuf.pklz --dynamic data/$seed/test.csv --out-file /dev/null
done
