# Using Machine Learning to predict the outcome of a zzuf fuzzing campaign

This repository contains all the technical details of [this tutorial](http://www.vdiscover.org/OS-fuzzing.html) on the use of [VDiscover](https://github.com/CIFASIS/VDiscover) including
 scripts and some data. The process to reproduce the results roughly follow these scripts:

0. init.sh
1. get_testcases.sh (*)
2. get_crashes.sh 
3. get_features.sh
4. test_predictor.sh

(*) It is recommended to run this command from a "sandbox" directory or user, just in case the tested command deletes or overwrite something important.

**Important:** most of scripts require to carefully check what files they need to read or write, and some tweaking as well.
Also, you should populate the seed directory before running the step 1.
