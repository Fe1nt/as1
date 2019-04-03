#!/usr/bin/python3

import sys


def tag_mapper():
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

        video_id = parts[0].strip()
        country = parts[11].strip()
        category = parts[3].strip()


            # In hadoop streaming, the output is sys.stdout, thus the print command
        print("{}\t{}\t{}".format(category, video_id, country))


if __name__ == "__main__":
    tag_mapper()
