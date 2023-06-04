# Compile

```g++ hirschberg.cpp -std=c++11```

# Validate algorithm

The test code generates 100,000 pairs of random strings (of lower case English alphabets) of size ranging from 1-100. For each pair of strings, the alignment is calculated using Hirschberg's algorithm and using Needleman-Wunsch algorithm. If there are multiple paths with same edit distance, it is possible that the two algorithms may give different alignments
for the same input. So correctness is tested as follows.
* If both algorithms give alignments with same edit distance AND
* If the alignments generated by Hirschberg's are valid alignments of the input strings (i.e, both alignments 
contain and only contain all the characters in the input strings and in the same order) AND
* If nowhere in the alignment a '-' is aligned with '-'

If for any of the test cases the correctness conditions fails, then the failed input strings alongwith the
output sequences generated by both algorithms are printed to stdout.

## To run the tests

```
./a.out unit-test
```

The test will take few minutes to complete.

# Run algorithm

To run algorithm for custom inputs there are multiple options.

## To run algorithm against custom inputs strings passed as commandline arguments

The output sequences will be printed to stdout. The memory and time consumed will be printed to stdout.

### Hirschberg's Algorithm
```
./a.out hirschberg <string1> <string2>
``` 
For example, 
```
./a.out hirschberg ABC BCA
```
Sample output, 
```
Memory usage: 128 MB
CPU time (system) used: 1.3e-05 seconds
CPU time (user) used: 3.8e-05 seconds
Elapsed time: 4.7e-05 seconds
ABC-
-BCA
```

### Needleman-Wunsch Algorithm
```
./a.out needleman-wunsch <string1> <string2>
``` 
For example, 
```
./a.out needleman-wunsch ABC BCA
```
Sample output, 
```
Memory usage: 124 MB
CPU time (system) used: 3e-06 seconds
CPU time (user) used: 1.3e-05 seconds
Elapsed time: 1.3e-05 seconds
ABC-
-BCA
```

## To run algorithm against custom inputs files passed as commandline arguments 

The output sequences will be written to a file named 'output.txt'. The memory and time consumed will be printed to stdout.

### Hirschberg's Algorithm
```
./a.out hirschberg --file <file1> <file2>
``` 
For example, 
```
./a.out hirschberg --file inputs/dna1.txt inputs/dna2.txt
```

### Needleman-Wunsch Algorithm
```
./a.out needleman-wunsch --file <file1> <file2>
``` 
For example, 
```
./a.out needleman-wunsch --file inputs/dna1.txt inputs/dna2.txt
```

## To run algorithm against randomly generated input strings (over English lowercase alphabet) of specified length

The output sequences will be written to a file named 'output.txt'. The memory and time consumed will be printed to stdout.

### Hirschberg's Algorithm
```
./a.out hirschberg --length <length1> <length2>
``` 
For example, 
```
./a.out hirschberg --length 1000 100
```

### Needleman-Wunsch Algorithm
```
./a.out needleman-wunsch --length <length1> <length2>
``` 
For example, 
```
./a.out needleman-wunsch --length 1000 100
```


# Performance tests

* The script `tests/test1.sh` was used to measure impact on memory and time consumed when string lengths
of both string1 and string2 increase equally.

* The script `tests/test2.sh` was used to measure impact on memory and time consumed when string length
of one string increase while the other is kept constant.

* The script `tests/test3.sh` was used to measure impact on memory and time consumed on real/artificial strings
of different symbol size.

* The script `tests/test4.sh` was used to measure impact on memory and time consumed on 100% same/different strings.

## To run

### Tests 1 and 2

```
. ./tests/test1.sh
```

```
. ./tests/test2.sh
```

### Test 3 and 4

Make sure you have all the input files, with names as specified in the test file, in the folder inputs/

```
. ./tests/test3.sh
```

```
. ./tests/test4.sh
```

## Outputs

Outputs of previous tests are saved in outputs/ folder.

Generated graphs of previous tests are saved in generate-graphs/ folder.

The python code in generate-graphs was used to plot the results of the previous tests. The values were hard-coded in the code for graph creation.