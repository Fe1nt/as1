#!/usr/bin/python3
import sys

def mapper():
    for line in sys.stdin:
        parts = line.strip().split(",")
        if len(parts) != 12:
            continue
        category = parts[3].strip()
        video_id = parts[0].strip()
        country = parts[11].strip()

        print("{}\t{}\t{}".format(category, video_id, country))

if __name__ == "__main__":
    mapper()
