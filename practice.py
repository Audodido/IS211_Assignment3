import argparse
import csv
from urllib.request import urlopen
from urllib.parse import unquote

def practice(url):
##download 
    # csvData = urlopen(url).read().decode('utf-8','ignore')
    # # print(type(csvData)) 
    # return csvData   

    response = urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    data = csv.reader(lines)
    for row in data:
        print(row)

# def processData(str):

#     reader = csv.reader(str, delimiter=',')
#     for row in reader:
#         print(row)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    practice(args.url)
    # processData(practice(args.url))

