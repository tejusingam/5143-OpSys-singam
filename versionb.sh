#!/bin/bash
ffile=$1
fname=$(basename $ffile)
fbname=${fname%.*}
DATE=`date +%Y-%m-%d`
dest="/singamt@cs2:~/5143_Opsys$file1.txt"
a="${dest##*.}"
result="$fbname"_"$DATE"."$a"
echo $result
cp $fname $result


