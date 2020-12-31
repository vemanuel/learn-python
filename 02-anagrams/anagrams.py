"""
anagrams.py: prompt user for input and display all anagrams of the selected letters.
Example Usage:
    python anagrams.py

Victor M. Emanuel
31-Dec-2020
"""

# *****************************************************************************
def get_input():
    """Prompt user for input."""
    letters = input('Enter letters, Enter to quit:\n')
    return letters

# *****************************************************************************
def load_words():
    """
    Load scrabble dictionary and create anagrams dict with
    key= sorted letters, value= list of anagrams
    Example:
        {
            'act': ['act', 'cat', 'tac']
            'dgo': ['dog', 'god'],
        }
    """
    # Load all the words from the scrabble dictionary into a python list, words
    fname = 'words.txt'
    with open(fname) as fh:
        words = fh.readlines()
    
    # Create a python dict keyed by sorted letters, with value equal to a list
    # of all the anagrams of that collection of letters
    anagrams = dict()
    for word in words:
        pass
    return anagrams

# *****************************************************************************
def main():
    """Console program."""
    # Load the anagrams dictionary
    anagrams = load_words()
    
    # Keep processing input from the user until they decide to quit
    while True:
        letters = get_input()
        if len(letters) > 0:
            print(f'You chose:\n{letters}\n')
        else:
            quit_prompt = input('Quit? Enter to confirm.')
            if len(quit_prompt) == 0:
                break
    
# *****************************************************************************
if __name__ == '__main__':
    main()
