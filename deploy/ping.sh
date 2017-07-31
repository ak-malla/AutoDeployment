#!/bin/bash
while read line
do
ping -c 1 $line; echo $line - $?
done < $1
