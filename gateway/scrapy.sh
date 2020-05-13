#!/bin/sh
for file in `find ./myscrapy/myscrapy/spiders -type f -name "*.py"`;do
echo $file
#sh $file
done