#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t")


def tag_reducer():
    """ This mapper select tags and return the tag-owner information.

    Note: Unlike normal hadoop which provide the reducer with key and a list of the values
        e.g. tag1, (owner1, owner2...)
    , hadoop streaming instead provide the reducer with sorted (key, value) lines
        e.g. tag1, owner1
             tag1, owner2
             ...

    Furthermore, unlike normal hadoop which calls the reducer for every key,
    in hadoop streaming multiple keys maybe given to the reducer
        e.g. tag1, owner1
             tag1, owner2
             tag2, owner2
             tag2, owner3
             tag3, owner1

    Input format: tag \t owner
    Output format: tag \t {owner=count}
    """
    current_category = ""
    category_count = []  # this is a list

    for category, video_id, country in read_map_output(sys.stdin):
        if category=="category":
            continue
        # Check if the tag read is the same as the tag currently being processed
        if current_category != category:

            # If this is the first line (indicated by the fact that current_tag will have the default value of "",
            # we do not need to output tag-owner count yet
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

            # Reset the tag being processed and clear the owner_count dictionary for the new tag
            current_category = category
            category_count.append([video_id, country])

        category_count.append([video_id, country])
        # owner_count[owner] = owner_count.get(owner, 0) + 1

    # We need to output tag-owner count for the last tag. However, we only want to do this if the for loop is called.
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


if __name__ == "__main__":
    tag_reducer()
