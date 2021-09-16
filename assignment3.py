#The url: http://s3.amazonaws.com/cuny-is211-spring2015/weblog.cs
import argparse
import csv
import datetime
import re
import sys
from urllib.request import urlopen

def downloadData(url): 
    """Downloads data and writes it to a locally-stored .csv"""

    response = urlopen(url)#.read()
    with open('weblog.csv', 'w') as new_file: #creates a file called weblog if there isn't one already in my directory
        new_file.write(response.read().decode('utf-8'))
    

def processData():
    """reads from my locally stored weblog.csv"""

    with open('weblog.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        data = [r for r in reader]
        for d in data:
            print(d) # changing this to 'return' later -- printing now just to see what's in 'data' variable
            print(type(data))

def main(url):
    print(f"Running main with URL = {url}...")

    downloadData(url)
    processData()


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
