from pprint import pprint


message = "the quick brown fox jumps over the lazy dog"

counter = {}
for letter in message:
    counter.setdefault(letter, 0)
    counter[letter] = counter[letter] + 1

pprint(counter)