#!/bin/bash -e
export name=$1
export link=$2
echo $name
echo $link

mkdir $name
cp example/* $name
echo $link >> $name/README