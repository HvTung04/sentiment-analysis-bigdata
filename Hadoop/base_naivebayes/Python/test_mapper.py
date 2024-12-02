import re
import sys
from collections import defaultdict

word_counts = defaultdict(lambda: [0, 0])

with open("train_output/out.txt", "r") as file:
    for line in file:
        key, value = line.strip().split("\t")
        if key == "NEG_DOC_COUNT":
            NEG_DOC_COUNT = int(value)
        elif key == "POS_DOC_COUNT":
            POS_DOC_COUNT = int(value)
        else:
            word_counts[key] = list(map(int, value.split("@")))

# Calculate prior prob
POS_PRIOR_PROB = POS_DOC_COUNT / (POS_DOC_COUNT + NEG_DOC_COUNT)
NEG_PRIOR_PROB = NEG_DOC_COUNT / (POS_DOC_COUNT + NEG_DOC_COUNT)

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

    words = tweet_text.split()

    # Calculate likelihood
    POS_LIKELIHOOD = 1
    NEG_LIKELIHOOD = 1
    for word in words:
        if word in word_counts:
            POS_LIKELIHOOD *= (word_counts[word][0] + 1) / (POS_DOC_COUNT + len(word_counts))
            NEG_LIKELIHOOD *= (word_counts[word][1] + 1) / (NEG_DOC_COUNT + len(word_counts))
        else:
            POS_LIKELIHOOD *= 1 / (POS_DOC_COUNT + len(word_counts))
            NEG_LIKELIHOOD *= 1 / (NEG_DOC_COUNT + len(word_counts))
    predicted_label = 1 if POS_PRIOR_PROB * POS_LIKELIHOOD > NEG_PRIOR_PROB * NEG_LIKELIHOOD else 0

    print(f"{sentiment}\t{predicted_label}")