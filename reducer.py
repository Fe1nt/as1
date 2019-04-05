#!/usr/bin/python3
import sys

current_category = ""
category_count = []

def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")

def outprint():
    current_category = ""
    category_count = []
    if current_category != "":
        output = current_category + "\t"
        category_count = list(set([tuple(t) for t in category_count]))
        category_count = [list(v) for v in category_count]
        num_country = len(category_count)
        s = []
        for video in category_count:
            s.append(video[0])
        s = set(s)
        num_video = len(s)
        average = num_country / num_video
        output += "{},".format(average)
        print(output.strip())

def reducer():
    current_category = ""
    category_count = []
    for category, video_id, country in read_map_output(sys.stdin):
        if category == "category":
            continue
        # Check if the tag read is the same as the tag currently being processed
        if current_category != category:
            outprint()
        current_category = category
        category_count.append([video_id, country])
    category_count.append([video_id, country])
    outprint()

if __name__ == "__main__":
    reducer()

