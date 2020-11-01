import sys


def main():

    try:
        plainText = sys.argv[1]
    except IndexError:
        plainText = input('plainText:')

    for text in plainText:
        if ord(text)<ord('a'): # Uppercase or lowercase
            ciperText = chr(ord('Z')-ord(text)+ord('A'))
        else:
            ciperText = chr(ord('z')-ord(text)+ord('a'))
        print(ciperText, end='')

    print()

if __name__=='__main__':
    main()

