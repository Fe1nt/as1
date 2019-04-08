#!/usr/bin/python3

import sys


def cate_mapper():
    """ This mapper select tags and return the tag-owner information.
    Input format: photo_id \t owner \t tags \t date_taken \t place_id \t accuracy
    Output format: tag \t owner
    """
    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split(",")

        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        if len(parts) != 12:
          continue

        category = parts[3].strip().split()
        videoID= parts[0].strip().split()
        country = parts[11].strip().split()

        
        print("{}\t{}\t{}".format(category, videoID,country))

if __name__ == "__main__":
    cate_mapper()
