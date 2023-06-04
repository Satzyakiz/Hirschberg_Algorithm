#!/bin/sh

echo "\n***************** Hirshberg *****************"
echo "\nUnary String 1 50KB X Unary String 1 50KB"
./a.out hirschberg --file inputs/unary1-50KB.txt inputs/unary0-50KB.txt
echo "\nUnary String 1 50KB X Unary String 0 50KB"
./a.out hirschberg --file inputs/unary1-50KB.txt inputs/unary0-50KB.txt