from pprint import pprint
from time import time

message = "the quick brown fox jumped over the lazy dog"

counter = {}
for letter in message:
    counter.setdefault(letter, 0)
    counter[letter] = counter[letter] + 1

pprint(counter)