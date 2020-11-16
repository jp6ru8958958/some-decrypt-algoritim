import sys

def caesar(cipherText):
    for text in cipherText:
        if ord(text)>=ord('A') and ord(text)<=ord('Z'):
            if ord(text)<=ord('C') and ord(text)>=ord('A') or ord(text)<=ord('c') and ord(text)>=ord('a'):
                plainText = chr(ord(text)+26-3)
            else:
                plainText = chr(ord(text)-3)
            print(plainText, end='')
        else:
            print(text, end='')
    return

def atbash(cipherText):
    for text in cipherText:
        if ord(text)>=ord('A') and ord(text)<=ord('Z'):
            if ord(text)<ord('a'):
                plainText = chr(ord('Z')-ord(text)+ord('A'))
            print(plainText, end='')
        else:
            print(text, end='')
    return

def A1Z26(cipherText):
    cipherText = cipherText.split(' ')
    for text in cipherText:
        split_cipherText_by_Dash = text.split('-')
        for mainText in split_cipherText_by_Dash:
            try:
                print(chr(int(mainText)+ord('A')-1), end='')
            except ValueError:
                print(mainText, end='')

        print(' ', end='')
    return

def vigenere(cipherText, key):
    keyPos = 0
    plaintext = ''
    for text in cipherText:
        if ord(text)>=ord('A') and ord(text)<=ord('Z'):
            plaintext = chr((ord(text) - ord(key[keyPos % len(key)])) % 26 + 65)
            keyPos+=1
            print(plaintext, end='')
        else:
            print(text, end='')
    return


if __name__ == '__main__':
    decrypt_way = sys.argv[1]
    cipherText = input('Ciphertext: ')
    if decrypt_way == 'caesar':
        caesar(cipherText)
    elif decrypt_way == 'atbash':
        atbash(cipherText)
    elif decrypt_way == 'a1z26':
        A1Z26(cipherText)
    elif decrypt_way == 'vigenere':
        key = input('KEY:')
        vigenere(cipherText, key)


'''
caesar:
ZHOFRPH WR JUDYLWB IDOOV

atbash:
HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.

a1z26:
2-21-20 23-8-15 19-20-15-12-5 20-8-5  3-1-16-5-18-19?

vigenere:
MXNGVEECW MW SLAWW. SUL FPZSK MW SOJMRX.
ERASE

a1z26 -> atbash -> caesar:
4-16-19 11-23-10 20-9-1-10-5-4-23-15-6-5 15-5 2-19-6-25 21-12-19-2-19-6
21-23-10 16-19 16-15-20-19 16-15-5 8-12-23-10-5 18-9-6-19-2-19-6 ?
'''