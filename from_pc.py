import words
import pc

if __name__ == '__main__':
    print(">>> QRL metal cold storage tool <<<")
    print("Please paste your metal cold storage binary seed (bigendian, 12 bits per word, each punch or mark = 1, blank = 0):")
    b = input()
    print("Here is your mnemonic seed phrase:")
    print(pc.bin_to_mnemonic(b))
