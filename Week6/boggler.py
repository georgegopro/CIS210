"""
Boggle solver finds words on a boggle board. 
Authors:  yuanw
Credits: #No

Usage:  python3 boggler.py  "board" dict.txt
    where "board" is 16 characters of board, in left-to-right reading order
    and dict.txt can be any file containing a list of words in alphabetical order
    
"""

from boggle_board import BoggleBoard   
import argparse   # Command line processing
import game_dict  # Dictionary of legal game words
import sys #Command line args

global results
def main():
    """
    Main program: 
    Find all words of length 3 or greater on a boggle 
    board. 
    Args:
        none (but expect two arguments on command line)
    Returns: 
        Nothing (but prints found words in alphabetical
        order, without duplicates, one word per line)
    """
    dict_file, board_text = getargs()
    game_dict.read( dict_file )
    board = BoggleBoard(board_text)
    global results
    results = [] 
    l = [0,1,2,3]
    for r in l:
        for c in l:
            find_words(board, r, c)
    comeout = duplicate(results)
    total = 0
    for word in comeout:
        numb = score(word)
        total += numb
        print(word + " " + str(numb))
    print("Total score: " + str(total))
        


def getargs():
    """
    Get command line arguments.
    Args:
       none (but expects two arguments on program command line)
    Returns:
       pair (dictfile, text)
         where dictfile is a file containing dictionary words (the words boggler will look for)
         and   text is 16 characters of text that form a board
    Effects:
       also prints meaningful error messages when the command line does not have the right arguments
   """
    parser = argparse.ArgumentParser(description="Find boggle words")
    parser.add_argument('board', type=str, help="A 16 character string to represent 4 rows of 4 letters. Q represents QU.")
    parser.add_argument('dict', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # will get arguments from command line and validate them
    text = args.board
    dictfile = args.dict
    if len(text) != 16 :
        print("Board text must be exactly 16 alphabetic characters")
        exit(1)
    return dictfile, text


        
def find_words(board, row=0, col=0, prefix=""):
    """Find all words starting with prefix that
    can be completed from row,col of board.
    Args:
        row:  row of position to continue from (need not be on board)
        col:  col of position to continue from (need not be on board)
        prefix: looking for words that start with this prefix
        results: list of words found so far
    Returns: nothing
        (side effect is filling results list)
    Effects:
        inserts found words (not necessarily unique) into results
    """
    global results
    if not board.available(row,col):
        return
    ch = board.get_char(row,col)
    prefix = prefix + ch
    if game_dict.search(prefix) == 1:
        results.append(prefix)
        board.mark_taken(row, col)
    elif game_dict.search(prefix) == 2:
        board.mark_taken(row, col)
    else:
        prefix = prefix[:len(prefix) - 1]
        return
    #checking th squares around
    find_words(board, row-1, col, prefix)
    find_words(board, row-1, col+1, prefix)
    find_words(board, row, col+1, prefix)
    find_words(board, row+1, col+1, prefix)
    find_words(board, row+1, col, prefix)
    find_words(board, row+1, col-1, prefix)
    find_words(board, row, col-1, prefix)
    find_words(board, row-1, col-1, prefix)
    board.unmark_taken(row, col)

def duplicate(list):
    """Remove duplicate
    then sort list
    Args:
        dict: a list which have to remove duplicate.
    Return:
          return a list called result.
   
    """
    result = [ ]
    prev = ""
    for word in list:
        if word != prev:
            result.append(word)
            prev = word
    result.sort()
    return result
    
    
def score(word):
    """
    Compute the Boggle score for a word, based on the scoring table
    at http://en.wikipedia.org/wiki/Boggle. 
    Args:
        word: A string with 3 or more letters.
    Return:
        Must an integer between 1 and 11.
     """
    long = len(word)
    if long == 3 or long == 4:
        return 1
    elif long ==5:
        return 2
    elif long == 6:
        return 3
    elif long == 7:
        return 5
    elif long > 8:
        return 11
    



####
# Run if invoked from command line
####

if __name__ == "__main__":
    main()
    input("Press enter to end")
