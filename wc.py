import sys
import os

def validate_args(args):
    if len(args) == 1:
        return args[0]
    elif len(args) == 2:
        return args[0], args[1]
    elif len(args) == 3:
        return args[0], args[1], args[2]
    else:
        raise ValueError('Too many arguments')

def wc_bytes(file):
    return os.stat(file).st_size
    
def wc_lines(file):
    return len(open(file).readlines())

def wc_words(file):
    with open(file) as file:
        return len(file.read().split())

if __name__ == '__main__':
    args = validate_args(sys.argv)
    if args[1] == '-c':
        print(wc_bytes(args[-1]), args[-1])
    elif args[1] == '-l':
        print(wc_lines(args[-1]), args[-1])
    elif args[1] == '-w':
        print(wc_words(args[-1]), args[-1])