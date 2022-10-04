# Punchcard
Python functions to convert mnemonic or hexseed to and from binary for use with a metal punchcard.

# Usage
Within a terminal, clone the repo to your local machine and directory with: `git clone https://github.com/surg0r/punchcard`

Move into the punchcard directory: `cd punchcard`

To convert from qrl mnemonic or hexseed: `python to_pc.py`

Paste your hexseed or mnemonic phrase and the tool outputs your binary seed.

Typical output:
```
>>> QRL metal cold storage tool <<<

Please paste your QRL seedphrase/mnemonic or hexseed:

absorb drank rodent label swap member heaven noise win gut city genre she beard excuse basic feudal apex monkey cowboy viral offer tin earn lose sight nylon and revest tray khowar sum bag aha

Binary output for metal cold storage tool (1 = punch/mark, 0= leave blank):

000000010000 010000000000 101110011110 011110001011 110110111111 100010011110 011001111000 100101100100 111110100111 011000110111 001010100100 010111000000 110001010101 000100111000 010010100100 000100100100 010011101111 000010011010 100011110001 001100011111 111100111110 100110010011 111001011101 010000110111 100000100011 110010000001 100110000001 000010000100 101101100111 111010010100 011101110010 110110101010 000100000010 000001001010
```

To convert from punchcard binary seed to mnemonic phrase: `python from_pc.py`

Paste your binary seed and the tool outputs your mnemonic phrase.

Typical output:
```
>>> QRL metal cold storage tool <<<

Please paste your metal cold storage binary seed (bigendian, 12 bits per word, each punch or mark = 1, blank = 0):

000000010000 010000000000 101110011110 011110001011 110110111111 100010011110 011001111000 100101100100 111110100111 011000110111 001010100100 010111000000 110001010101 000100111000 010010100100 000100100100 010011101111 000010011010 100011110001 001100011111 111100111110 100110010011 111001011101 010000110111 100000100011 110010000001 100110000001 000010000100 101101100111 111010010100 011101110010 110110101010 000100000010 000001001010

Here is your mnemonic seed phrase:

absorb drank rodent label swap member heaven noise win gut city genre she beard excuse basic feudal apex monkey cowboy viral offer tin earn lose sight nylon and revest tray khowar sum bag aha
```

