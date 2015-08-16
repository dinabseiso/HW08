#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################

def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(dictionary, sought_value):
    matches = list()
    # try:                                          # Could be kept if we did not already know that all the values were numbers.
    # 	type(int(sought_value)) == "int"
    # 	sought_value = int(sought_value)
    # except ValueError :
    # 	pass
    for key in dictionary:                          # A dictionary is scanned in a for loop by keys, not by values. For does not see the values.
        if dictionary[key] == sought_value :
        	matches.append(key)                    # If a match is found between a value and our value of interest, add the key to list full of matches.
    # return sorted(k for k, value in dictionary.items() if matches[value] == value)
    return matches

def histogram_new(s):
    pledge_histogram = {}
    for c in s:                                                 # For every word in the pledge_list returned below...
        pledge_histogram[c] = pledge_histogram.get(c,0) + 1     # Check to see if the word is a key in our new, empty dictionary. Add a tally either way.
    return pledge_histogram

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open("pledge.txt", "r") as fin:
        a = fin.read().replace(',','').replace(".","").replace(":","")  # Could not think of a better way to get rid of punctuation.
        pledge_list = [ word for word in a.split()] 
        return pledge_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################




##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, 1)
    print reverse_lookup_new(pledge_histogram, 9)
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
