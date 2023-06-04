#!/bin/sh

#!/bin/sh

lengths=(100 1000 2000 5000 8000 10000 20000)

echo "\n***************** Hirschberg *****************"
for length in ${lengths[@]}; do
  echo "\nLengths $length X $length"
  ./a.out hirschberg --length $length $length
done

echo "\n************** Needleman-Wunsch **************"
for length in ${lengths[@]}; do
  echo "\nLengths $length X $length"
  ./a.out needleman-wunsch --length $length $length
done

echo "\nDone"
