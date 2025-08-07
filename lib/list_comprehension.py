#!/usr/bin/env python3

# Return even numbers
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

# Add exclamation marks
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
