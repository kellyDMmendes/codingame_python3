''' Binary with 0 and 1 is good, but binary with only 0, or almost, is even
better!
Write a program that takes an incoming message as input and displays as output
the message encoded using this method. '''
binary = []
CRYPTO = ""
CODE = ""

message = input()
for i, msg in enumerate(message):
    bit = list(bin(ord(msg)))
    bit.remove('b')
    if msg.isalpha():
        zero = bit.index("1")
        bit = bit[zero:]
    binary += bit

BNR0 = ""
for i, bnr in enumerate(binary):
    if bnr == "0":
        if i == 0:
            CRYPTO += "00 "
            CRYPTO += "0"
        elif bnr != BNR0:
            CRYPTO += " 00 "
            CRYPTO += "0"
        else:
            CRYPTO += "0"
    else:
        if i == 0:
            CRYPTO += "0 "
            CRYPTO += "0"
        elif bnr != BNR0 or i == 0:
            CRYPTO += " 0 "
            CRYPTO += "0"
        else:
            CRYPTO += "0"
    BNR0 = bnr
CODE += CRYPTO

print(CODE)
