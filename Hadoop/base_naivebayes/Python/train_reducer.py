import sys
from collections import defaultdict

word_counts = defaultdict(lambda: [0, 0])
NEG_DOC_COUNT = 0
    
for line in sys.stdin:
    key, value = line.strip().split("\t")
    sentiment_label = value
    if sentiment_label == "POSITIVE":
        word_counts[key][0] += 1
    elif sentiment_label == "NEGATIVE":
        word_counts[key][1] += 1
    else:
        if key == "NEG_DOC_COUNT":
            NEG_DOC_COUNT += int(value)
        elif key == "POS_DOC_COUNT":
            POS_DOC_COUNT = int(value)

# Output the word frequencies for positive and negative sentiment
for word, counts in word_counts.items():
    print(f"{word}\t{counts[0]}@{counts[1]}")

# Output the document counts
print(f"NEG_DOC_COUNT\t{NEG_DOC_COUNT}")
print(f"POS_DOC_COUNT\t{POS_DOC_COUNT}")