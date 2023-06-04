#!/bin/sh

lengths=(1000 1000000 2000000 5000000 10000000 20000000 50000000 100000000)
fixed_length=10

echo "\n***************** Hirschberg *****************"
for length in ${lengths[@]}; do
  echo "\nLengths $length X $fixed_length"
  ./a.out hirschberg --length $length $fixed_length
done

echo "\n************** Needleman-Wunsch **************"
for length in ${lengths[@]}; do
  echo "\nLengths $length X $fixed_length"
  ./a.out needleman-wunsch --length $length $fixed_length
done

echo "\nDone"
