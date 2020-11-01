import sys


def main():

    try:
        plainText = sys.argv[1]
    except IndexError:
        plainText = input('plainText:')

    for text in plainText:
        if ord('c')>=ord(text) and ord(text)>=ord('a') or ord('C')>=ord(text) and ord(text)>=ord('A'):
            ciperText = chr(ord(text)+26-3)
        else:
            ciperText = chr(ord(text)-3)

        print(ciperText, end='')

    print()

if __name__=='__main__':
    main()

