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
            print(chr(int(mainText)+ord('A')-1), end='')
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
    cipherText = input('Plaintext:')
    if decrypt_way == 'caesar':
        caesar(cipherText)
    elif decrypt_way == 'atbash':
        atbash(cipherText)
    elif decrypt_way == 'a1z26':
        A1Z26(cipherText)
    elif decrypt_way == 'vigenere':
        key = input('KEY:')
        vigenere(cipherText, key)
