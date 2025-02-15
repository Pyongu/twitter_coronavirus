#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--output_path',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top10Items = items[10::-1]
print(top10Items)
top10CL = []
top10Num = []
for i in range(len(top10Items)):
    kvTuple = items[i]
    k = kvTuple[0]
    v = kvTuple[1]
    top10CL.append(k)
    top10Num.append(v)
print(top10CL)
print(top10Num)

# making bar plot
plt.bar(top10CL, top10Num, color = 'green')
plt.title(f'Top 10 Values for { args.key}')
plt.xlabel(f'{args.input_path}')
plt.savefig(args.output_path)
