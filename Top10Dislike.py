from pyspark import SparkContext
from ml_utils import *
import argparse

if __name__ == "__main__":
    sc = SparkContext(appName="Top10Disklike")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path")
    parser.add_argument("--output", help="the output path")
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output

    Original = sc.textFile("AllVideos_short.csv")
    filtedInfo = Original.map(filtering)
    integrated = filtedInfo.map(counting)
    records = integrated.groupByKey().map(lambda x : (x[0], list(x[1])))

    list1=[]
    for s in records.collect():
        grade=0
        if len(s[1])>=2:
            grade=int(s[1][1][1])-int(s[1][0][1])
            category=s[1][0][0]
            video_ID_country=s[0]
            list1.append((video_ID_country, [category,grade]))

    result=sc.parallelize(list1).map(changeKey).sortByKey(0).top(10)
    sc.parallelize(result).map(formatTrans).saveAsTextFile(output_path)
    
