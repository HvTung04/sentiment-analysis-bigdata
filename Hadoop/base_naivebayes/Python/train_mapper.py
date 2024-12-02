import re
import sys

NEG_DOC_COUNT = 0
POS_DOC_COUNT = 0

# Regular expression for cleaning tweet text
url_pattern = re.compile(r"(?i)(https?:\/\/(?:www\.)?[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]+|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]+)")
mention_hashtag_pattern = re.compile(r"(#|@|&).*?\w+")
non_alpha_pattern = re.compile(r"[^a-zA-Z ]")

for line in sys.stdin:
    # Clean up the tweet
    columns = line.strip().split(",")
    if len(columns) > 4:
        columns[3] = "".join(columns[3:])
    sentiment = columns[1]
    tweet_text = columns[3]
    
    # Clean the tweet text
    tweet_text = url_pattern.sub("", tweet_text)  # remove URLs
    tweet_text = mention_hashtag_pattern.sub("", tweet_text)  # remove mentions/hashtags
    tweet_text = non_alpha_pattern.sub(" ", tweet_text)  # remove non-alphabetic characters
    tweet_text = tweet_text.lower()  # convert to lowercase

    # Count sentiment and word frequency
    sentiment_label = "POSITIVE" if sentiment == "1" else "NEGATIVE"
    if sentiment_label == "POSITIVE":
        POS_DOC_COUNT += 1
    else:
        NEG_DOC_COUNT += 1

    words = tweet_text.split()

    # Emit words with sentiment label
    for word in words:
        print(f"{word}\t{sentiment_label}")
    
# Emit document count
print(f"NEG_DOC_COUNT\t{NEG_DOC_COUNT}")
print(f"POS_DOC_COUNT\t{POS_DOC_COUNT}")