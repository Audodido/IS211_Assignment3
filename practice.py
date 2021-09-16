import argparse
import csv
from urllib.request import urlopen

def practice(url):

    # response = urlopen(url).read()

    with urlopen(url) as response:
        response = response.read()
        reader = csv.reader(response.decode('utf-8'), delimiter=",")
        for line in reader:
            print(line)
    # data = [row for row in reader]
    # for d in data:
    #     print(d)



        #for line in data:
            #print(line)
            # line = line.decode('utf-8')
            # print(line)






if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    practice(args.url)

