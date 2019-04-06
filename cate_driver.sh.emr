#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./cate_driver.sh [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Tag owner inverted list' \
-file cate_mapper.py \
-mapper cate_mapper.py \
-file cate_reducer.py \
-reducer cate_reducer.py \
-input $1 \
-output $2
