import sys
from collections import defaultdict

word_counts = defaultdict(lambda: [0, 0])
    
for line in sys.stdin:
    key, value = line.strip().split("\t")
    sentiment_label = value
    if sentiment_label == "POSITIVE":
        word_counts[key][0] += 1
    else:
        word_counts[key][1] += 1

# Output the word frequencies for positive and negative sentiment
for word, counts in word_counts.items():
    print(f"{word}\t{counts[0]}@{counts[1]}")
