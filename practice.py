#The url: http://s3.amazonaws.com/cuny-is211-spring2015/weblog.cs
#path to file, datetime accessed, browser, status of request, request size in bytes
import argparse
import csv
import datetime
import re
import sys
from urllib.request import urlopen

def downloadData(url): 
    """Pulls down web log file """

    response = urlopen(url) # don't have to write out 'url.lib.request.urlopen()' because of how I imported -- lil bit cleaner
    lines = [l.decode('utf-8') for l in response.readlines()] #decoding and putting lines from file into a list
    return lines


def processData(lines):

    img_index = 0
    total_index = 0


    data = csv.reader(lines)

    for row in data:
        total_index += 1
        x = re.search("PNG|JPG|GIF$", row[0], re.IGNORECASE)
        if bool(x) == True:
            img_index += 1

    percent_of_img = round(img_index / total_index, 2)    
    message = "Image requests account for {}% of all requests".format(percent_of_img)

    print(message)





def main(url):
    print(f"Running main with URL = {url}...")

    #downloadData(url)
    processData(downloadData(url))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
