#!/usr/bin/python3
import sys
def read_map_output(file):

    for line in file:
        yield line.strip().split("\t")


def cate_reducer():

    current_category = ""
    category_list = []

    for category, videoID, country  in read_map_output(sys.stdin):
       
        if category =="category" :
            continue
        if current_tag != category:
            if current_category !="":
                category_list=list(set([tuple(t) for t in category_list]))
                category_list = [list(v) for v in category_list]
                output = current_category  + "\t"
                for item in range(len(category_list)):
                    category_videolist.append(item[0])
                category_videolist = list(set(category_videolist))
                average = ("%.2f"%(float(len(category_list)))/float(len(category_videolist)))
                output +="{},".format(average)
                print(output.strip())
            category_list = []
            current_category = category
        category_list.append([videoID,country])

    if current_category !="":
        category_list=list(set([tuple(t) for t in category_list]))
        category_list = [list(v) for v in category_list]
        output = current_category  + "\t"
        for item in range(len(category_list)):
            category_videolist.append(item[0])
        category_videolist = list(set(category_videolist))
        average = ("%.2f"%(float(len(category_list)))/float(len(category_videolist)))
        output +="{},".format(average)
        print(output.strip())

if __name__ == "__main__":
    cate_reducer()
