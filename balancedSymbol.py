import Stack

def matching_symb(symbl):
    """def is to define a method
    This method will take an input and see if there is a balance of open and close symbols"""

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

