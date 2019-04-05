#!/usr/bin/python3
import sys

def cate_mapper():
    for line in sys.stdin:
        parts = line.strip().split(",")
        if parts.len() != 12:
            continue
        category = parts[3].strip().split()
        video_id = parts[0].strip().split()
        country = parts[11].strip().split()

        print("{}\t{}\t{}".format(category, video_id, country))

if __name__ == "__main__":
    cate_mapper()
