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
    letters = input('Enter letters:\n')
    return letters

# *****************************************************************************
def main():
    """Console program."""
    letters = get_input()
    print(f'You chose:\n{letters}')

# *****************************************************************************
if __name__ == '__main__':
    main()
