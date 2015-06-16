# OS-fuzzing

There are the scripts and data to perform fuzzing at large scale and to predict 
The process to reproduce the results roughtly follow these scripts

0. init.sh
1. get_testcases.sh (*)
2. get_crashes.sh 
3. get_features.sh
4. test_predictor.sh

(*) It is recommended to run this command from a "sandbox" directory or user, 
just in case the tested command deletes or overwrite something important.
