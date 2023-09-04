# Creating command line utility in python | Python Tutorial - Day #85

import argparse

parser=argparse.ArgumentParser()

# Add command line arguments

parser.add_argument('url',help='Url of the file to download')
parser.add_argument('output',help='by which name do you wnat to save your file')

# parse the arguments
arge=parser.parse_args()

# Use the arguments in ypur code

print(arge.url)
print(arge.output)





