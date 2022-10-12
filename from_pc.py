import words
import pc

if __name__ == '__main__':
    print("\n>>> QRL metal cold storage tool <<<\n\n")
    print("Please paste your metal cold storage binary seed (bigendian, 12 bits per word, each punch or mark = 1, blank = 0):\n")
    b = input()
    print("\nHere is your mnemonic seed phrase:\n")
    print(pc.bin_to_mnemonic(b), "\n")
