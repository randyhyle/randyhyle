#  File: TestCipher.py
#  Description: A program that can encode and decode using the Rail
#  Fence method and the Vigenere method.
#  Student's Name: Hoang Randy Hy Le
#  Student's UT EID: hhl385
#  Partner's Name:
#  Partner's UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 9/11/2021
#  Date Last Modified: 9/14/2021

import sys


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    print('Plain Text:', strng)
    print('Key:', key)
    # Create the encoded rail fence
    rail_fence = create_rail_fence_encode(strng, key)
    encoded_railfence = ''
    # Through each row iteration, add the characters to the string
    # as long as it is an alphabetic character
    for row in rail_fence:
        for col in row:
            if col != '-':
                encoded_railfence += col

    return encoded_railfence


def create_rail_fence_encode(strng, key):
    """Function that creates the rail fence cipher and encodes the
    given string into a 2D list. Returns a 2D list."""
    # Create empty rail fence
    rail_fence = [['-' for _ in range(len(strng))] for _ in range(key)]
    num_of_chs = len(strng)
    row = 0
    col = 0
    for i in range(num_of_chs):
        rail_fence[row][col] = strng[i]
        # Check if the current row is the very top row
        if row == 0:
            row += 1
            col += 1
        # Else check if the current row is at the very bottom
        elif row == len(rail_fence) - 1:
            row -= 1
            col += 1
        # Else check if there is a value occupying the spot to the
        # top left of the current row and column
        elif row > 0 and rail_fence[row - 1][col - 1] != '-':
            row += 1
            col += 1
        # Check if there is a value occupying the spot to the bottom
        # left of the current row and column
        elif rail_fence[row + 1][col - 1] != '-':
            row -= 1
            col += 1

    return rail_fence


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    print('Enter Key:', key)
    empty_rail_fence = create_rail_fence_decode(strng, key)
    rail_fence = fill_rail_fence_cipher(strng, key, empty_rail_fence)

    decoded_rail_fence = ''
    row = 0
    col = 0
    for i in range(len(strng)):
        decoded_rail_fence += rail_fence[row][col]
        if row == 0:
            row += 1
            col += 1
        elif row == len(rail_fence) - 1:
            row -= 1
            col += 1
        elif row > 0 and rail_fence[row - 1][col - 1] != '-':
            row += 1
            col += 1
        elif rail_fence[row + 1][col - 1] != '-':
            row -= 1
            col += 1

    return decoded_rail_fence


def create_rail_fence_decode(strng, key):
    """Function that creates a rail fence cipher with the string
    '*' to mark the places where the string should go. Returns a 2D
    list."""
    rail_fence = [['-' for _ in range(len(strng))] for _ in range(key)]
    num_of_ch = len(strng)
    row = 0
    col = 0
    for i in range(num_of_ch):
        rail_fence[row][col] = '*'
        if row == 0:
            row += 1
            col += 1
        elif row == len(rail_fence) - 1:
            row -= 1
            col += 1
        elif row > 0 and rail_fence[row - 1][col - 1] != '-':
            row += 1
            col += 1
        elif rail_fence[row + 1][col - 1] != '-':
            row -= 1
            col += 1
    return rail_fence


def fill_rail_fence_cipher(strng, key, rail_fence):
    """Function that fills the empty spots denoted by an '*' with the
    characters in a string."""
    strng_index = 0
    # Fill in the cipher where the string should be.
    for i in range(key):
        for j in range(len(strng)):
            if rail_fence[i][j] != '-':
                rail_fence[i][j] = strng[strng_index]
                strng_index += 1

    return rail_fence


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    strng = strng.lower()
    new_string = ''
    for ch in strng:
        if ch.isalpha():
            new_string += ch
    return new_string


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character(p, s):
    # Record the shift in characters
    shift = ord(p) - ord('a')

    encoded_ch = ''
    # If ordinal of s + shift exceeds the ord z we want to reset to
    # ord a and keep counting the leftover shift
    if ord(s) + shift > ord('z'):
        difference = -(ord('z') - (ord(s) + shift))
        encoded_ch += chr(ord('a') + difference - 1)
    # Otherwise, add the ord of s with shift to get our new character
    else:
        encoded_ch += chr(ord(s) + shift)

    return encoded_ch


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character(p, s):
    # Reverse the shift
    reverse = ord(s) - ord(p)

    decoded_ch = ''
    # If the reversal ends up being negative, add 26 to the reversal
    # then add that sum to the ordinal a to get our decoded character.
    if reverse < 0:
        reverse += 26
        decoded_ch += chr(ord('a') + reverse)
    else:
        decoded_ch += chr(ord('a') + reverse)

    return decoded_ch


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    print('Plain Text:', strng)
    print('Pass Phrase:', phrase)
    # Create a key phrase that matches in length with the string by
    # looping the phrase over and over.
    key_phrase = create_key(strng, phrase)

    encoded_text = ''
    for i in range(len(key_phrase)):
        encoded_text += encode_character(key_phrase[i], strng[i])

    return encoded_text


def create_key(strng, phrase):
    """Function that creates the key to match the plain text for the
    Vigenere Cipher."""
    key_phrase = ''
    if len(strng) != len(phrase):
        for i in range(len(strng) - len(key_phrase)):
            key_phrase += phrase[i % len(phrase)]
    return key_phrase


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    print('Pass Phrase:', phrase)
    # Create a key phrase that matches in length with the string by
    # looping the phrase over and over.
    key_phrase = create_key(strng, phrase)

    decoded_text = ''
    for i in range(len(key_phrase)):
        decoded_text += decode_character(key_phrase[i], strng[i])
    return decoded_text


def main():
    # read the plain text from stdin
    plain_text = sys.stdin.readline().rstrip()
    # read the key from stdin
    key = int(sys.stdin.readline())

    # encrypt and print the encoded text using rail fence cipher
    print('Rail Fence Cipher\n')
    encoded_plain_text = rail_fence_encode(plain_text, key)
    print('Encoded Text:', encoded_plain_text)
    print()

    # read encoded text from stdin
    encoded_text = sys.stdin.readline().rstrip()
    # read the key from stdin
    key = int(sys.stdin.readline())

    # decrypt and print the plain text using rail fence cipher
    print('Encoded Text:', encoded_text)
    decrypted_encoded_text = rail_fence_decode(encoded_text, key)
    print('Decoded Text:', decrypted_encoded_text)
    print()

    # read the plain text from stdin
    vigenere_plain_text = sys.stdin.readline().rstrip()
    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline().rstrip()

    # encrypt and print the encoded text using Vigenere cipher
    print('Vigenere Cipher\n')
    encoded_plain_text = vigenere_encode(vigenere_plain_text, pass_phrase)
    print('Encoded Text:', encoded_plain_text)
    print()

    # read the encoded text from stdin
    vigenere_encoded_text = sys.stdin.readline().rstrip()
    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline().rstrip()
    # decrypt and print the plain text using Vigenere cipher
    print('Encoded Text:', vigenere_encoded_text)
    vig_decrypted_text = vigenere_decode(vigenere_encoded_text, pass_phrase)
    print('Decoded Text:', vig_decrypted_text)


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
