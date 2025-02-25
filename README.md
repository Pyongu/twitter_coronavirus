# Coronavirus twitter analysis

The code in this repo was for a project for CSCI-143, Big Data at Claremont McKenna College. It uses the MapReduce method in order to analyze tweets about Coronavirus in 2020. 

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
In total, there are about 1.1 billion tweets in this dataset.


## MapReduce

[MapReduce](https://en.wikipedia.org/wiki/MapReduce) is done in three main steps: Partition, Map, and Reduce. The partition step was already done for by Professor Izbicki. The tweets were spilt up into into one file per day

**Map:**

The map step created a nested dictionary that kept track of the different coronavirus related hashtags and the country or language that it was in and the total count. This step was run on each file.

**Reduce:**

The reduce step took all of the dictionarys that the map step created for each day and combined them into one large dictionary that had all of the coronavirus tweek information for the entire year.

**Visualizer:**

After mapping and reducing the data, I used matplotlib to visualize the data. This was done by creating two lists from the dictionary that had the language/country and the counts for them which were used for the X and Y axes. I decided to plot #coronoavirus and #코로나바이러스(Coronavirus in Korean).

<img src=src/corona_language.png>
<img src=src/corona_country.png>
<img src=src/korean_language.png>
<img src=src/korean_country.png>

Overall we can see that #coronoavirus was used heavily in the United States and in the English language. But it also had a large presence in other countries and languages. On the other hand, #코로나바이러스 was bascially only used in Korea and Korean.

## Alternate Reduce

I also used an alternative way to MapReduce the coronavirus tweek data. For each related hashtag, I kept track of the number of times that someone tweeted and coronavirus related hashtag for each day. I did this by using a nested dictionary that kept track of the hashtag and the date and its count. Then I also visualized it using matplotlib where the X-axis is the date, Y-axis is the count, and each line is a different hashtag. I decided to plot the coronavirus related hashtags: #doctor, #flu, #sick.
<img src=src/alt_reduce.png>

Overall, most of theses hashtags aren't used a lot daily. However one interesting part of this data, is the large spike of #doctor at around June 29, 2020. 

