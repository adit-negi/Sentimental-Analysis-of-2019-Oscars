import csv
from collections import defaultdict
import re
from textblob import TextBlob

columns = defaultdict(list)  # each value in each column is appended to a list

with open('blackkklansman_r.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        for (i, v) in enumerate(row):
            columns[i].append(v)
tweets = columns[4]

tweet = []
for j in tweets:

    x = ' '.join(
        re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", j).split())
    tweet.append(x)


average_polarity = 0
lenght = len(tweet)
for i in tweet:
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    print(polarity)
    average_polarity = (average_polarity+polarity)
print(average_polarity/lenght)
print(lenght)
