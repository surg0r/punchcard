import words
import pc

if __name__ == '__main__':
    print("\n>>> QRL metal cold storage tool <<<\n\n")
    print("Please paste your QRL seedphrase/mnemonic or hexseed:\n")
    s = input()
    if len(s) == 102:
        s = pc.hexseed_to_mnemonic(s)
    print("\nBinary output for metal cold storage tool (1 = punch/mark, 0= leave blank):\n")
    print(pc.mnemonic_to_bin(s), "\n")
