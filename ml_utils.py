import csv

"""
This module includes a few functions used in computing average rating per genre
"""


def filtering(record):
    try:
        columns = record.split(",")
        videoID = columns[0]
        category = columns[3]
        likes = columns[6]
        dislikes = columns[7]
        country = columns[11]
        gap=int(dislikes)-int(likes)

        key = videoID + country
        value = [category, gap]
        return (key, value)
    except:
        return ()

def changeKey(a):
    videoID=a[0]
    category=a[1][0]
    grade=a[1][1]

    key = grade
    value = [category,videoID]

    return (key, value)

