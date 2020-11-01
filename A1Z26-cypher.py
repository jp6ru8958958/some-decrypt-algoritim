import sys


def main():

    plainText = input('plainText:')

    plainText = plainText.split(' ')

    for text in plainText:
        print(chr(int(text)+ord('A')-1), end='')

    print()

if __name__=='__main__':
    main()

