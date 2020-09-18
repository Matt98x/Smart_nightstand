#!/bin/bash

echo "Write the name of the gif"
read a
echo "Write the name of folder containing the png-converted gif"
read b

mkdir ./background_animation/$b
cd ./background_animation/$b
pwd
convert -verbose -coalesce ../../gifs/$a %03d.png
