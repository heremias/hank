#!/bin/bash
$ICOUNT=$(ls | wc -l)
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
# set me
FILES=$(/data/*)
for f in $FILES
do
  echo "$f"
done
# restore $IFS
IFS=$SAVEIFS