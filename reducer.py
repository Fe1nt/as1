#!/usr/bin/python3
import sys

def read_map_output(file):
    for line in file:
        yield line.strip().split("\t", 2)


def reducer():
    current_category = ""
    categoryList = []
    for category, video_id, country in read_map_output(sys.stdin):
        if category == "category":
            continue
        if current_category != category:
            outprint(current_category,categoryList)
        current_category = category
        categoryList = []
    categoryList.append([video_id, country])
    outprint(current_category,categoryList)


def outprint(current_category,categoryList):
    categoryVideoList = []
    if current_category != "":
        categoryList = list(set([tuple(t) for t in categoryList]))
        categoryList = [list(v) for v in categoryList]
        output = current_category + "\t"
        for item in range(categoryList.len()):
            categoryVideoList.append(item[0])
        categoryVideoList = list(set(categoryVideoList))
        average = len(categoryList) / len(categoryVideoList)
        output += "{},".format(average)
        print(output.strip())

if __name__ == "__main__":
    reducer()

