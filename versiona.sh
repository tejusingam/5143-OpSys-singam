#!/bin/bash
sample=$1
DATE=`date +%Y-%m-%d`
modified="$DATE"_"$sample"
echo $modified
cp $sample $modified

