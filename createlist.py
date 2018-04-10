#!/usr/bin/python
#coding=utf-8
import sys, argparse, os

parser = argparse.ArgumentParser(
        description='Extract specific information from a list, and create a new one with the information.', 
        usage="Arrays start at 0 folks..", 
        prog="G3V4L14"
        )
parser.add_argument('-f', type=str, help="The file you want to extract from")
parser.add_argument('-d', type=str, help="Delimiter")
parser.add_argument('-c', type=int, help="Pick a column")
args = parser.parse_args()

class clr:
    B = "\033[0;92m"
    W = "\033[0m"

txt = open(args.f, 'r')
newfile = open('brute.txt', 'w+')
delimiter = args.d
col = args.c


i = 0
with txt as f:

    first_line = f.readline()
    first_split = first_line.split(delimiter)
    #print(enumerate(first_split))
    print(first_split)

    for line in f:
        new = line.split(delimiter)
        print(str(i)+clr.B+new[col]+clr.W),
        newfile.write(new[col])
        i += 1

print('\n\n')
print(str(i) + " words filtered")
print('\n'+"Removing duplicates: Please wait!")
os.system('cat brute.txt | uniq -u > new.txt')
os.system('wc -l new.txt')

