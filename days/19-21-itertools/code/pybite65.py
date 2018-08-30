import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('.\\tmp', 'dictionary.txt')
# urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    real_words = []
    words = _get_permutations_draw(draw)
    for item in words:
        if item.lower() in dictionary:
            real_words.append(item.lower())

    return real_words


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    words = []
    for i in range(3, len(draw) + 1):
        possible_permutations = itertools.permutations(draw, i)
        possible_words = [''.join(map(str, words)) for words in
                          possible_permutations]
        for word in possible_words:
            words.append(word)
    return words


if __name__ == "__main__":
    foo = get_possible_dict_words(['T', 'I', 'I', 'G', 'T', 'T', 'L'])
    for item in foo:
        print(item)
