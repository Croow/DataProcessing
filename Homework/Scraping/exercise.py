# Name :
# Student number :
'''
This module contains an implementation of split_string.
'''

# You are not allowed to use the standard string.split() function, use of the
# regular expression module, however, is allowed.
# To test your implementation use the test-exercise.py script.

# A note about the proper programming style in Python:
#
# Python uses indentation to define blocks and thus is sensitive to the
# whitespace you use. It is convention to use 4 spaces to indent your
# code. Never, ever mix tabs and spaces - that is a source of bugs and
# failures in Python programs.


def split_string(source, separators):
    '''
    Split a string <source> on any of the characters in <separators>.

    The ouput of this function should be a list of strings split at the
    positions of each of the separator characters.
    '''
    split_string = []                       # Create list for the splitted string
    remainder_source = str( source )
    if source:                              # Check if source contains elements
        if separators:                      # Check if separators contain elements
            first_character = True          # Boolean that checks if we are working with the first character of the remainder of the source
            st = ''                         
            for letter in source:           # Loop over source
                count = 0                   
                for separator in separators:            # Loop over separators
                    count += 1                          # Count the number of separators checked
                    if letter == separator:             # Check if letter of source equals to the separator
                        if first_character:             # If it is the first character of the remainder of the source: remove character
                            remainder_source = remainder_source[1:]
                        else:                           # If not: append ST to SPLIT_STRING and remove first character of the remainder of the source
                            split_string.append( st )
                            st = ''
                            remainder_source = remainder_source[1:]
                            first_character = True       # We are back to the first character
                        break
                    else:                   # If letter does not equals separator: append letter to ST, remove the character of remainder source and set FIRST_CHARACTER to false
                        if count == len( separators ):
                            st += remainder_source[0]
                            remainder_source = remainder_source[1:]
                            first_character = False
                            break
            if st:                          # If soucre does not end with separator: append remainder to SPLIT_STRING
                split_string.append( st )
        else:                               # If no separators are mentioned append SOURCE to SPLIT_STRING
            split_string.append( source )
    return split_string


                


if __name__ == '__main__':
    # You can try to run your implementation here, that will not affect the
    # automated tests.
    print split_string('abacadabra', 'b')
