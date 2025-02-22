#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys', nargs='+', required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    date = path[18:26]
    with open(path) as f:
        tmp = json.load(f)
        for keys in args.keys:
            total[keys][date] += sum(tmp[keys].values())
for hashtags in args.keys:
    sorted_dict = sorted(total[hashtags].items())
    keys = []
    values = []
    for k,v in sorted_dict:
        keys.append(k)
        values.append(v)
    plt.plot(keys, values, label = hashtags)

dates = sorted(total[args.keys[0]].keys())
ticks = dates[::15]
plt.title("Daily Tweet Counts for Selected Hashtags")
plt.xlabel("Date")
plt.ylabel("Count")
plt.xticks(ticks, rotation=80)
plt.subplots_adjust(bottom=0.2)
plt.legend()
plt.savefig(args.output_path)
