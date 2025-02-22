#!/bin/sh

for file in '/data/Twitter dataset/'geoTwitter20-*.zip; do
    python map.py --input_path "$file" &
done
