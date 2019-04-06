from pyspark import SparkContext
from ml_utils import *
import argparse

if __name__ == "__main__":
    sc = SparkContext(appName="Caonima")
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
            grade=s[1][1][1]-s[1][0][1]
            category=s[1][0][0]
            video_ID=s[0]
            list1.append((video_ID, [category,grade]))

    result=sc.parallelize(list1).map(changeKey).sortByKey(False).take(10)
    sc.parallelize(result).saveAsTextFile(output_path)
    
