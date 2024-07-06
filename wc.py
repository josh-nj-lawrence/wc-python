import sys
import argparse
import os

# Functions for each switch
def wc_bytes(file):
    with open(file, 'rb') as file:
        return len(file.read())
    
def str_bytes(s):
    return len(s.encode('utf-8'))
    
def wc_lines(file):
    return len(open(file).readlines())

def str_lines(s):
    return s.count('\n')

def wc_words(file):
    with open(file) as file:
        return len(file.read().split())

def str_words(s):
    return len(s.split())
    
def wc_chars(file):
    with open(file) as file:
        return len(file.read())
    
def str_chars(s):
    return len(s)
    
def main():
    parser = argparse.ArgumentParser(description='Linux WC tool remade in python')
    parser.add_argument('files', nargs='*', help='Files to process')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='Print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='Print the word counts')
    parser.add_argument('-m', '--chars', action='store_true', help='Print the character counts')
    args = parser.parse_args()

    
    # Check for no switch case
    default = False
    if not (args.words or args.lines or args.bytes or args.chars):
        default = True

    # Check for stdin case
    if not args.files and not sys.stdin.isatty():
        # Stdin has input, process it
        input_text = sys.stdin.read()
        if args.bytes:
            print(str_bytes(input_text))
        if args.lines:
            print(str_lines(input_text))
        if args.words:
            print(str_words(input_text))
        if args.chars:
            print(str_chars(input_text))
        if default:
            print(str_bytes(input_text), str_lines(input_text), str_words(input_text))
    
    else:
        # Process all files for input
        for file in args.files:
            try:
                if args.bytes:
                    print(wc_bytes(file), file)
                if args.lines:
                    print(wc_lines(file), file)
                if args.words:
                    print(wc_words(file), file)
                if args.chars:
                    print(wc_chars(file), file)
                if default:
                    print(wc_bytes(file), wc_lines(file), wc_words(file), file)
            except Exception as e:
                print(f"Error processing {file}: {e}")


if __name__ == '__main__':
    main()