
import os
import sys
import csv
import random


from sklearn import cross_validation

data_filename = sys.argv[1]
seed = sys.argv[2]

data_dir = "data/"+seed
train_filename = data_dir+"/train.csv"
test_filename = data_dir+"/test.csv"

os.system("mkdir -p "+data_dir)

random.seed(seed)

programs = dict()
vuln_programs, norm_programs = dict(), dict()
vuln_testcases, norm_testcases = dict(),dict()

csv.field_size_limit(sys.maxsize)

# we read the list of all programs
with open(data_filename, 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1, delimiter='\t')
    
    for i,row in enumerate(reader1):
      if (len(row) <> 3):
        continue
           
      if  (row[2] == '1'):
        vuln_testcases[row[0]] = 1
        vuln_programs[row[0].split(":")[0]+":"] = 1

      elif  (row[2] == '0'):
        norm_testcases[row[0]] = 1
        norm_programs[row[0].split(":")[0]+":"] = 1

      programs[row[0].split(":")[0]+":"] = 1

#print vuln_testcases.keys(), len(vuln_testcases.keys())
#print norm_testcases.keys(), len(norm_testcases.keys())

#vuln_size, norm_size = len(vuln_programs.keys()), len(norm_programs.keys())
prog_size = len(programs.keys())

#print vuln_programs.keys()
#print norm_programs.keys()

#vuln_sample = random.sample(vuln_programs.keys(), vuln_size) 
#norm_sample = random.sample(norm_programs.keys(), norm_size) 

prog_sample = random.sample(programs.keys(), prog_size) 
train_prop = 0.75

train_programs = prog_sample[:int(train_prop*prog_size)]
test_programs  = prog_sample[int(train_prop*prog_size):]

# we read the list of all programs
with open(data_filename, 'rb') as csvfile1:
 with open(train_filename, 'wb') as csvfile2:
  with open(test_filename, 'wb') as csvfile3:

    reader1 = csv.reader(csvfile1, delimiter='\t')
    train_csv = csv.writer(csvfile2, delimiter='\t')
    test_csv = csv.writer(csvfile3, delimiter='\t')

    for i,row in enumerate(reader1):
      if (len(row) <> 3):
        continue
      if row[0].split(":")[0]+":" in train_programs:
        train_csv.writerow(row)
      elif row[0].split(":")[0]+":" in test_programs:
        test_csv.writerow(row)
      else:
        assert(0)

one_out = random.sample(vuln_programs.keys(), 1)[0]

#print one_out
 
train_programs = filter(lambda prog: not (one_out in prog), prog_sample)
test_programs  = [one_out]

train_filename = data_dir+"/train-one-out.csv"
test_filename = data_dir+"/test-one-out.csv"

# we read the list of all programs
with open(data_filename, 'rb') as csvfile1:
 with open(train_filename, 'wb') as csvfile2:
  with open(test_filename, 'wb') as csvfile3:

    reader1 = csv.reader(csvfile1, delimiter='\t')
    train_csv = csv.writer(csvfile2, delimiter='\t')
    test_csv = csv.writer(csvfile3, delimiter='\t')

    for i,row in enumerate(reader1):
      if (len(row) <> 3):
        continue
      if row[0].split(":")[0]+":" in train_programs:
        train_csv.writerow(row)
      elif row[0].split(":")[0]+":" in test_programs:
        test_csv.writerow(row)
      else:
        assert(0)
 

