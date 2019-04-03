import sys
import csv


def mapper():

    for line in csv.reader(sys.stdin):
        # parts = line.strip().split("\t")
        parts = line
        if len(parts) != 12:
            continue

        vedio_id = parts[0].strip()
        category = parts[3].strip()
        country = parts[-1].strip()

        print("{}\t{}".format(category, vedio_id+"..."+country))
        # print("{}\t{}\t{}".format(category, vedio_id, country))
        # 要么传三个值，第一个默认key，后边两个value
        # 要么传两个值，第一个key，后一个value


if __name__ == "__main__":
    mapper()
