#!/bin/sh

echo "\n***************** Hirshberg *****************"
echo "\nDNA Sequence 1 24KB X DNA Sequence 2 24KB"
./a.out hirschberg --file inputs/dna1-24KB.txt inputs/dna2-24KB.txt
echo "\nDNA Sequence 1 24KB X DNA Sequence 1 24KB"
./a.out hirschberg --file inputs/dna1-24KB.txt inputs/dna1-24KB.txt
echo "\Protein Sequence 1 24KB X Protein Sequence 2 24KB"
./a.out hirschberg --file inputs/protein1-24KB.txt inputs/protein2-24KB.txt
echo "\Protein Sequence 1 24KB X Protein Sequence 1 24KB"
./a.out hirschberg --file inputs/protein1-24KB.txt inputs/protein1-24KB.txt
echo "\nRandom String 1 24KB X Random String 2 24KB"
./a.out hirschberg --file inputs/random1-24KB.txt inputs/random2-24KB.txt
echo "\nRandom String 1 24KB X Random String 1 24KB"
./a.out hirschberg --file inputs/random1-24KB.txt inputs/random1-24KB.txt

echo "\n************** Needleman-Wunsch **************"
echo "\nDNA Sequence 1 24KB X DNA Sequence 2 24KB"
./a.out needleman-wunsch --file inputs/dna1-24KB.txt inputs/dna2-24KB.txt
echo "\nDNA Sequence 1 24KB X DNA Sequence 1 24KB"
./a.out needleman-wunsch --file inputs/dna1-24KB.txt inputs/dna1-24KB.txt
echo "\Protein Sequence 1 24KB X Protein Sequence 2 24KB"
./a.out needleman-wunsch --file inputs/protein1-24KB.txt inputs/protein2-24KB.txt
echo "\Protein Sequence 1 24KB X Protein Sequence 1 24KB"
./a.out needleman-wunsch --file inputs/protein1-24KB.txt inputs/protein1-24KB.txt
echo "\nRandom String 1 24KB X Random String 2 24KB"
./a.out needleman-wunsch --file inputs/random1-24KB.txt inputs/random2-24KB.txt
echo "\nRandom String 1 24KB X Random String 1 24KB"
./a.out needleman-wunsch --file inputs/random1-24KB.txt inputs/random1-24KB.txt
echo "\nDone"
