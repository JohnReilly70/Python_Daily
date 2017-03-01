from itertools import permutations

def letter_permutation(string, word_len):
    perm_list = []
    while word_len <= len(string):
        perm_list.append([perm for perm in permutations(string,word_len)])
        word_len += 1
    print(perm_list)

letter_permutation('helol',2)