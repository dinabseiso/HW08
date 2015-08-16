#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

def invert_dict_old(d):
    inverse = dict()                                
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    """ For looking at both keys and values in a list of tuples, 
    check the dictionary inverse to see whether a certain value exists. 
    If not, then create a default sub-value to be associated with it. 
    Every additional key found to have that value will be appended to 
    create a list of items associated with that value.

    Please note that the result of this function is a dictionary with
    tallies not as values as they previously were in predecessor dictionaries, 
    but as keys. What were once keys are now the associated values. 
    """   
    inverse = {}
    for key, val in d.items():                          
        inverse.setdefault(val, []).append(key)
    return inverse


def print_hist_newest(h):
    for i in range(max(h)):             # From 0 to the largest key found in the passed in dictionary...
        i+=1                            # Start i at 1.
        if h.get(i, None) == None :     # If the key i returns None, and thus cannot be found...
            h[i] = []                   # Create a field for that key, and assign it an empty value.
    return h

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(s):
    dictionary = {}
    for c in s:
        dictionary[c] = dictionary.get(c,0) + 1
    return dictionary

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open("pledge.txt", "r") as fin:
        a = fin.read().replace(',','').replace(".","").replace(":","")
        pledge_list = [ word for word in a.split()] 
        return pledge_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)


if __name__ == '__main__':
    main()
