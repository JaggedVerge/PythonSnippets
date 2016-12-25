"""
This module is an implementation for a function that is an example
of the type of function we may wish to write a unit test for.

See the unit test file for how we can do that
"""

def example_function(filename):
    """
    Read the given file and create a list that contains each line as an item

    :filename: the file we are opening
    :return: a list of lines as taken from the file
    :rtype: list
    """
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line)
    return data
    
