import csv

"""
This module includes a few functions used in computing average rating per genre
"""


def filtering(record):
    try:
        columns = record.split(",")
        videoID = columns[0].strip()
        category = columns[3].strip()
        like = columns[6].strip()
        dislike = columns[7].strip()
        country = columns[11].strip()

        return ([videoID,category,like,dislike,country])
    except:
        return ()

def counting(lists):
    try:
        gap = int(lists[3]) - int(lists[2])
        key = lists[0]+lists[4]
        value = [lists[1],gap]
        return(key,value)
    except:
        return ('',[''])

def changeKey(a):
    videoID=a[0]
    category=a[1][0]
    grade=a[1][1]

    key = grade
    value = [category,videoID]
    return (key, value)

