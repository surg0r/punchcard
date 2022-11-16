from textwrap import wrap
import words

# this is a series of functions to manipulate qrl mnemonic or hexstring to and from 12 bit binary strings
# for the purpose of seed phrase storage and retrieval on a metal punch card

# standard QRL mnemonic extended seed has 34 words of 12 bits data each (4096 word list)
# first 3 bytes (two 12 bit words) are the extended seed - this is the 24 bit address descriptor
# the nibbles of each of the three bytes in this descriptor are reversed..
# next 48 bytes are random data


# returns a padded 12 bit binary string from a valid seed word
def word_to_bin(word):
    return str(bin(words.words.index(word.lower()))[2:]).rjust(12,'0')

# returns a word from a padded 12 bit binary string 
def bin_to_word(bin):
    return words.words[int(bin, 2)]

# returns a string of padded 12 binary strings from a valid case insensitive seed phrase list
def mnemonic_to_bin(seedphrase):
    s = seedphrase.split()
    b = []
    for word in s:
        b.append(word_to_bin(word))
    return " ".join(b)

# returns a mnemonic from a valid hexstring
def hexseed_to_mnemonic(hexseed):
    h = wrap(hexseed,3)
    m = []
    for nibbles in h:
        m.append(words.words[int(nibbles, 16)])
    return " ".join(m)

# returns hexstring from a valid mnemonic
def mnemonic_to_hexseed(mnemonic):
    s = mnemonic.split()
    h = []
    for word in s:
        h.append(hex(words.words.index(word.lower()))[2:].rjust(3,'0'))
    return "".join(h)

# returns a mnemonic from a string of padded 12 bit binary strings
def bin_to_mnemonic(bin):
    s = bin.split()
    m = []
    for b in s:
        m.append(bin_to_word(b))
    return " ".join(m)

