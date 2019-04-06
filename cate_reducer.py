#!/usr/bin/python3
import sys
def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")
def cate_reducer():
    current_category = ""
    category_count = []  # this is a list
    #for category, video_id, country in read_map_output(sys.stdin):
    for category, videoID, countryID in read_map_output(sys.stdin):

        if videoID=="video_id": # ignore the first row
            continue
        if category != current_category:
            if current_category != "":
                category_count = list(set([tuple(t) for t in category_count]))
                category_count = [list(v) for v in category_count]
                numCountry = len(category_count)
                list1 =[]
                for item in category_count:
                    video =item[0]
                    list1.append(video)
                list2 = []
                for id in list1:
                    if id not in list2:
                        list2.append(id)
                numVideo = len(list2)
                average =str(("%.2f" %(numCountry/numVideo)))
                print("{}\t{}".format(current_category, average).strip())   
            category_count = []
            current_category =category
        category_count.append([videoID,countryID])
    lastprint(current_category,category_count)

def lastprint(current_category,category_count):
    current_category = current_category
    category_count = category_count
    if current_category != "":
                category_count = list(set([tuple(t) for t in category_count]))
                category_count = [list(v) for v in category_count]
                numCountry = len(category_count)
                list1 =[]
                for item in category_count:
                    video =item[0]
                    list1.append(video)
                list2 = []
                for id in list1:
                    if id not in list2:
                        list2.append(id)
                numVideo = len(list2)
                average =str(("%.2f" %(numCountry/numVideo)))
                print("{}\t{}".format(current_category, average).strip())

if __name__ == "__main__":
    cate_reducer()

