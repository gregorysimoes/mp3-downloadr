#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2
import argparse


# parser arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', dest='input_path', type=str, help='mp3 file url')
parser.add_argument('-n', dest='file_name', type=str, help='file name', default="./francq.csv")

args = parser.parse_args()

# set an URL
url = args.input_path

# set a filename
mp3Name = args.file_name

req2 = urllib2.Request(url)
response = urllib2.urlopen(req2)
data = response.read()

song = open(mp3Name, "wb")
song.write(data)
song.close()
