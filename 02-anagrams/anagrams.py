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
def word_key(word):
    """Convert a word to a dictionary key."""
    key = ''.join(sorted(word))
    return key

# *****************************************************************************
def load_words():
    """
    Load scrabble dictionary and create a dict anagram_tbl with
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
    anagram_tbl = dict()
    for word in words:
        word_lc = word.rstrip().lower()
        key = word_key(word_lc)
        value = anagram_tbl.get(key, []) + [word_lc]
        anagram_tbl[key] = value
    return anagram_tbl

# *****************************************************************************
def load_defs():
    """Load word definitions as a python dict."""
    # Load word definitions
    fname = 'word-definitions.txt'
    with open(fname) as fh:
        lines = fh.readlines()
    
    # Create dictionary keyed by lowercase word
    def_tbl = dict()
    for line in lines:
        # split the dictionary line at the first space
        word, word_def = line.split(sep=None, maxsplit=1)
        # add this entry to the dictionary
        word = word.lower()
        def_tbl[word] = word_def.rstrip()
    return def_tbl

# *****************************************************************************
def find_anagrams(anagram_tbl, word):
    """Find all anagrams of a word."""
    key = word_key(word)
    anagrams = anagram_tbl.get(key, [])
    return anagrams

# *****************************************************************************
def main():
    """Console program."""
    # Load the anagrams dictionary
    anagram_tbl = load_words()
    # Load the definitions of the words
    def_tbl = load_defs()
    # Keep processing input from the user until they decide to quit
    while True:
        letters = get_input()
        if len(letters) > 0:
            #print(f'You chose:\n{letters}\n')
            anagrams = find_anagrams(anagram_tbl, letters)
            print(f'Anagrams of {letters.upper()}:')
            for word in anagrams:
                word_def = def_tbl[word]
                print(f'{word.upper()}: {word_def}')
            print()
        else:
            quit_prompt = input('Quit? Enter to confirm.')
            if len(quit_prompt) == 0:
                break
    
# *****************************************************************************
if __name__ == '__main__':
    main()
