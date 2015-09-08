# Name : Caroline Azeau
# Student number : 10334858
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

    # Create list for the splitted string 
    # and create a copy of SOURCE
    split_string = []
    remainder_source = str( source )

    # Check if SOURCE contains elements
    if source:

        # Check if SEPARATORS contain elements
        if separators:

            # Create a boolean that checks if we are working with
            # the first character of the rREMAINDER_SOURCE
            first_character = True
            st = ''

            # Loop over SOURCE          
            for letter in source:
                count = 0

                # Loop over SEPARATORS            
                for separator in separators:

                    # Count the number of separators checked        
                    count += 1

                    # Check if letter of source equals to the separator
                    if letter == separator:

                        # If it is the first character of REMAINDER_SOURCE: remove character
                        # If not: append ST to SPLIT_STRING and remove first character of REMAINDER_SOURCE
                        # and set FIRST_CHARACTER to TRUE
                        if first_character:
                            remainder_source = remainder_source[1:]
                        else:                           
                            split_string.append( st )
                            st = ''
                            remainder_source = remainder_source[1:]
                            first_character = True
                        break
                    # If LETTER does not equals SEPARATOR: append letter to ST, remove 
                    # the character of REMAINDER_SOURCE and set FIRST_CHARACTER to FALSE
                    else:
                        if count == len( separators ):
                            st += remainder_source[0]
                            remainder_source = remainder_source[1:]
                            first_character = False
                            break
            # If SOURCE does not end with a separator: append remainder to SPLIT_STRING
            if st:
                split_string.append( st )

        # If no separators are mentioned, append SOURCE to SPLIT_STRING
        else:
            split_string.append( source )

    # Return a list of the splitted string
    return split_string


                


if __name__ == '__main__':
    # You can try to run your implementation here, that will not affect the
    # automated tests.
    print split_string('abacadabra', 'b')
