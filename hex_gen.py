import random
import math
import nltk

# Download words
nltk.download('words')

from nltk.corpus import words
setofwords = set(words.words())


# Define hex length
hex_length = 8

# All possible hexadecimal charactor
hex_chars = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8",
    "9", "A", "B", "C", "D", "E", "F"
]
hex_speaks = [
    '0000000FF1CE', '00BAB10C', '1BADB002', '4B1D', '8BADF00D', 'ABADBABE', 
    'B105F00D', 'B16B00B5', '0B00B135', 'BAAAAAAD', 'BAADF00D', 'BAD22222', 
    'BADDCAFE', 'CAFEB0BA', 'B0BABABE', 'BEEFBABE', 'B000 DEAD', 'C00010FF', 
    'C15C:0D06:F00D', 'CAFEBABE', 'CAFED00D', 'CEFAEDFE', '0D15EA5E', 
    'DABBAD00', 'DEAD2BAD', 'DEADBAAD', 'DEADBABE', 'DEADBEAF', 
    'deadbeef-dead-beef-dead-beef00000075', 'DEADC0DE', 'DEADDEAD', 
    'DEADD00D', 'DEADFA11', 'DEAD10CC', 'DEADFEED', 'DECAFBAD', 'DEFEC8ED', 
    'D0D0CACA', 'E011CFD0', 'F1AC', 'face:b00c', 'FACEFEED', 'FBADBEEF', 'FEE1DEAD', 
    'FEEDBABE', 'FEEDC0DE', 'FEEDFACECAFEBEEF', 'FFBADD11', 'F00DBABE', '1337BEEF', 
    '1337F001', '1337BEEF', 'F00DBEEF', '1337C0D3', '1337BABE'
]

def is_consecutive_generation(string: str):
    """Check if string generated is consecutive."""
    # Load last index
    max_length = len(hex_chars)

    # Iterate checking
    for i in range(len(hex_chars)):
        # Generate compare list
        compare_list = (
            hex_chars[i:i+hex_length] if i + hex_length < max_length
            else hex_chars[i:] + hex_chars[:(i + hex_length - max_length)]
        )

        # Ignore if not match
        if "".join(compare_list) != string:
            continue

        return True
    
    return False


def is_repetitive_generation(string: str):
    """Check if string generated is repetitive."""
    # Tokenize string
    tokenized_string = [item for item in string]

    # Return check
    return len(set(tokenized_string)) <= 1


def is_common_words(string: str):
    """Check if string generated is commonly used word."""
    return string.lower() in setofwords


def is_hex_speak(string: str):
    """Check if string generated is commonly used word."""
    return string.lower() in hex_speaks


def random_hexadecimal():
    """Generate random 8 digit hex code."""
    # Check list
    check_list_methods = [
        is_consecutive_generation,
        is_repetitive_generation,
        is_common_words,
        is_hex_speak
    ]

    # Iterate generation
    while True:
        # Generate random index
        random_indexes = [
            math.floor(random.random() * 16) for i in range(8)
        ]

        # Generate hexadecimal string
        result = "".join([
            hex_chars[index] for index in random_indexes
        ])

        # Iterate check list
        is_valid = True
        for method in check_list_methods:
            # Ignore if check method fail
            if not method(result):
                continue

            # Set not valid if method check success
            is_value = False
            break

        # Validate result
        if not is_valid:
            continue

        # Report result
        print("Valid code generated: 0x%s" % result)

        return f"0x{result}"

if __name__ == "__main__":
    random_hexadecimal()
