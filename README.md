# OS-fuzzing

There are the scripts and data for the VDiscover tutorial to predict the outcome of zzuf. The process to reproduce the results roughtly follow these scripts:

0. init.sh
1. get_testcases.sh (*)
2. get_crashes.sh 
3. get_features.sh
4. test_predictor.sh

(*) It is recommended to run this command from a "sandbox" directory or user, just in case the tested command deletes or overwrite something important.

**Important:** most of scripts require to carefully check what files they need to read or write, and some tweaking as well.
Also, you should populate the seed directory before running the step 1.
