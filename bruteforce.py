import hashlib
import itertools

def bruteforce(passwordHash):

    wordlist = "abcdefghijklmnopqrstuvwxyz"
    y=''
    length=1
    wordlistHash=''

    while wordlistHash != passwordHash:
        for c in itertools.product(wordlist, repeat=length):
            word = y.join(c)
            wordlistHash = hashlib.sha3_512(word.encode("utf-8")).hexdigest()
            if wordlistHash == passwordHash:
                print(f"Found password: {word}")
                break
        length=length + 1

bruteforce('99fb8667d94c08080873cdde10c5e0430baa59752d9f1204c1305176c50601fb63b438bd92b8fff633e5bd9952f7d857eb3a97d9d24871e22ad2db1e86ea95a7')
