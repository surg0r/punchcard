import words
import pc 

if __name__ == '__main__':
    print ">>> QRL metal cold storage tool <<<"
    print "Please paste your QRL seedphrase/mnemonic or hexseed:"
    s = raw_input()
    if len(s) == 102:
        s = pc.hexseed_to_mnemonic(s)
    print "Binary output for metal cold storage tool (1 = punch/mark, 0= leave blank): "
    print pc.mnemonic_to_bin(s)
