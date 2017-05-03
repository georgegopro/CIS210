"""
Count the number of occurrences of each major code in a file.
Authors: yuanw
Credits: #FIXME

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    #FIXME:  This function needs a good docstring
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    #FIXME:  Your loop with 'control break logic' (including initialization)
    #        replaces this simple printing loop below. 
    count = 0
    for major in majors:
        print(major, count)

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
