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

    percent_of_img = int(round(img_index / total_index * 100))    
    message = "Image requests account for {}% of all requests".format(percent_of_img)

    print(message)


def browser_checker(lines):
    
    data = csv.reader(lines)

    chrome_index = 0
    firefox_index = 0
    ie_index = 0
    safari_index = 0

    for row in data:
        y = re.search("Chrome/*.*$", row[2], re.IGNORECASE)
        if bool(y) == True:
            print(y)
            chrome_index += 1

    for row in data:
        y = re.search("Firefox/*.*$", row[2], re.IGNORECASE)
        if bool(y) == True:
            firefox_index += 1

    # for row in data:
    #     y = re.search("MSIE|Trident", row[2], re.IGNORECASE)
    #     if bool(y) == True:
    #         ie_index += 1
    #         print(bool(y), row[2])

    # for row in data:
    #     y = re.search("Safari/*.*$", row[2], re.IGNORECASE)
    #     if bool(y) == True:
    #         safari_index += 1


    print("Chrome: ", chrome_index)
    print("Firefox: ", firefox_index)
    print("Internet Explorer: ", ie_index)
    print("Safari: ", safari_index)



def main(url):
    print(f"Running main with URL = {url}...")

    # downloadData(url)
    processData(downloadData(url))
    browser_checker(downloadData(url))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
