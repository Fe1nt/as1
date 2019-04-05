#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t")


def cate_reducer():
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
    category_list = []

    for category, videoID, country  in read_map_output(sys.stdin):
        # Check if the tag read is the same as the tag currently being processed
        if category =="category" :
            continue
            # If this is the first line (indicated by the fact that current_tag will have the default value of "",
            # we do not need to output tag-owner count yet
        if current_tag != category:
            outprint(current_category,category_list)
            category_list = []
            current_category = category
        category_list.append([videoID,country])
    outprint(current_category,category_list)




            # Reset the tag being processed and clear the owner_count dictionary for the new tag
            

    # We need to output tag-owner count for the last tag. However, we only want to do this if the for loop is called.
def outprint(current_category,category_list):
    category_videolist = []
    if current_category !="":
        category_list=list(set([tuple(t) for t in category_list]))
        category_list = [list(v) for v in category_list]
        output = current_category  + "\t"
        for item in range(len(category_list)):
            category_videolist.append(item[0])
        category_videolist = list(set(category_videolist))
        average = float(len(category_list))/float(len(category_videolist))
        output +="{},".format(average)
        print(output.strip())

if __name__ == "__main__":
    cate_reducer()
