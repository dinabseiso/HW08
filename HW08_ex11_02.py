#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports

# Body

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
    """ The ultimate goal of this function is to tally how many times
    a word appears in the list of words returned in get_pledge_list().
    This could be later used to make a nice histogram plot, which tallies
    the number of occurrences of a given thing."""

    dictionary = {}
    for c in s:                                     # s is the pledge_list being returned below. For every word in the list...
        dictionary[c] = dictionary.get(c,0) + 1     # See if c is a key in the empty dictionary. If not, create key c, and set the value to 0.
    return dictionary                               # If the key has already been added to the dictionary, increment the value by 1. 

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open("pledge.txt", "r") as fin:
        a = fin.read().replace(',','').replace(".","").replace(":","")
        pledge_list = a.split()                     # Cuts up the stanzas into a list of words, wherever there was a space (or whatever is designated to split by).
        return pledge_list

##############################################################################
def main():   # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())



if __name__ == '__main__':
    main()
