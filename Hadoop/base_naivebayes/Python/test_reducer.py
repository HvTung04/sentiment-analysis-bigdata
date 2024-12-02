import sys

accuracy = 0
total = 0

for line in sys.stdin:
    label, predicted_label = line.strip().split("\t")
    if label == predicted_label:
        accuracy += 1
    total += 1

print(f"Accuracy: {accuracy / total}")