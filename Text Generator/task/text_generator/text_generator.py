from nltk import bigrams
from collections import Counter
import random
import re

corpus_file = input()
with open(corpus_file, "r", encoding="utf-8") as corpus:
   tokens = corpus.read().split()
bigram_list = list(bigrams(tokens))

dictionary = {}
for head, tail in bigram_list:
   dictionary.setdefault(head, Counter())
   dictionary[head].update([tail])

cap_words = [word for word in tokens if word[0].isupper()]

sentences = []
while len(sentences) < 10:
   sentence = []
   first_word = random.choice(tokens)
   if not re.search(r'^[A-Z][a-z]+[^.?!]$', first_word):
      continue
   sentence.append(first_word)
   while len(sentence) < 5 or not re.search(r'[.?!]', sentence[-1]):
      last_word = sentence[-1]
      tail_list = list(dictionary[last_word].keys())
      freq_list = list(dictionary[last_word].values())
      next_word = random.choices(tail_list, weights=freq_list)[0]
      sentence.append(next_word)
   sentences.append(' '.join(sentence))
   print(*sentence)