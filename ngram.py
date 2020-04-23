__author__ = 'Keshan De Silva'

import re

from nltk.corpus import brown
from nltk.corpus import reuters
from collections import OrderedDict
from operator import itemgetter
from random import randint

unigrams = dict()
bigrams = dict()

wordonly_regex = re.compile('.*[A-Za-z].*')  # must contain a letter or digit
prev_word = " "

print('Reading Corpus')
for fileid in brown.fileids():
    print()
    print('Reading Field ', end='')
    for sentences in brown.sents(fileid):
        print('#', end='')

        for token in sentences:
            if wordonly_regex.match(token):
                token = token.lower()
                if token in unigrams:
                    unigrams[token] += 1
                else:
                    unigrams[token] = 1

                bigram = prev_word + ',' + token
                if bigram in bigrams:
                    bigrams[bigram] += 1
                else:
                    bigrams[bigram] = 1

                # change value of prev_word
                prev_word = token

print()
print('Corpus Read Complete')
print('Calculating Probabilities')
for key, value in bigrams.items():
    word = key.split(',')[0]
    if word in unigrams:
        total_count = unigrams[word]
        probability = value / total_count
    else:
        probability = 0
    bigrams[key] = probability

print('Sorting Data')
sorted_unigrams = OrderedDict(sorted(unigrams.items(), key=itemgetter(1), reverse=True))
sorted_bigrams = OrderedDict(sorted(bigrams.items(), key=itemgetter(1), reverse=True))

print('Generating unigram-result.txt File')
output_file = open('unigram-result.txt', 'w')
output_file.write("Uni-gram Model\n")
for key, value in sorted_unigrams.items():
    output_file.write(key + ':' + str(value) + '\n')
output_file.close()

print('Generating bigram-result.txt File')
output_file = open('bigram-result.txt', 'w')
output_file.write("Bi-gram Model\n")
for key, value in sorted_bigrams.items():
    output_file.write(key + ':' + str(value) + '\n')
output_file.close()

print('Random Sentence Generator')
sentence_count = 5
min_word_count = 3
max_word_count = 4

unigram_buffer_limit = 0
bigram_buffer_limit = 0
unigram_buffer_index = 0
bigram_buffer_index = 0

print('Converting Dictionaries')
unigram_key_list = list(sorted_unigrams.keys())
bigram_key_list = list(sorted_bigrams.keys())

for key, value in sorted_unigrams.items():
    unigram_buffer_index += 1
    if value < unigram_buffer_limit:
        break

for key, value in sorted_bigrams.items():
    bigram_buffer_index += 1
    if value < bigram_buffer_limit:
        break

for i in range(0, sentence_count):
    print('Generating Sentence')
    word_count = randint(min_word_count, max_word_count)
    sentence = list()
    word_index = randint(0, unigram_buffer_index)
    pre_word = unigram_key_list[word_index]
    sentence.append(pre_word)
    probability = 1

    j = 0
    while len(sentence) < word_count:
        for k in range(j, bigram_buffer_index):
            word_pair = bigram_key_list[k]
            word = word_pair.split(',')[0]
            if word == pre_word:
                j = k
                pre_word = word_pair.split(',')[1]
                sentence.append(pre_word)
                probability *= sorted_bigrams.get(word_pair)
                break

    print(sentence)
    print(probability)

print('DONE')