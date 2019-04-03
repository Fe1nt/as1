import sys
import csv


def read_map_output(file):
    for line in file:
        yield line.strip().split("\t", 1)          #要么传三个值，第一个默认key，后边两个value，这里写2分两次
                                                   #要么传两个值，第一个key，后一个value，这里写1分一次


def reducer():
    list1=[]
    list2=[]
    value1=0
    value2=0
    current_category=""
    output=""
    result=0
    #有些没用的可以去掉应该

    for category, vedio_id_country in read_map_output(sys.stdin):          #传3传2都可以
        l = vedio_id_country.strip().split("...")          #传3个才用到，配合mapper一起， 用2个去掉直接写就好
                                                           #如果用这种，下面list1.append([[l[0],l[1]])
        if category == "category":                         #              list2.append(l[0])
            continue

        if current_category != category:
            if current_category != "":
                output = current_category
                list1 = list(set(tuple(t) for t in list1))          #注意这里set去重的用法
                list1 = [list(v) for v in list1]                    #同上
                value1 = len(list1)

                list2 = list(set(tuple(t) for t in list2))
                list2 = [list(v) for v in list2]
                value2 = len(list2)

                result = ("%.2f" %(value1 / value2))
                res = str(result)
                output = output + ":" + res          #float数不能直接和str+一起
                print("{}".format(output))
                value1 = 0
                value2 = 0
                result = 0
                list1 = []
                list2 = []

        current_category = category
        list1.append([l[0], l[1]])          #append里一次只能加一个obj，可以为数组[a,b,c]
        list2.append(l[0])          #list.append之后不能再赋值给list(不能写在一起)

    if current_category != "":          #注意逻辑位置
        output = current_category
        list1 = list(set(tuple(t) for t in list1))
        list1 = [list(v) for v in list1]
        value1 = len(list1)
        list2 = list(set(tuple(t) for t in list2))
        list2 = [list(v) for v in list2]
        value2 = len(list2)
        result = ("%.2f" % (value1 / value2))          #这里的操作和上边循环一样
        res = str(result)
        output = output + ":" + res
        print("{}".format(output))


if __name__ == "__main__":
    reducer()
