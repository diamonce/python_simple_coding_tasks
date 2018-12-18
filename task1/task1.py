"""Summ of values in array"""
import sys

import array as arr

a = arr.array('i', [2, 4, 6, 8])

def add_for():
    """Add numbers using for."""
    rez = 0

    for x in a:
        rez += x

    print(rez);

    pass


def add_while():
    """Add numbers using while."""
    rez = 0
    i = 0
    while i < len(a):
        rez += a[i]
        i = i + 1 

    print(rez);

    pass


def add_recur(rez, i):
    """Add numbers using recursion."""

    if i < len(a):
        rez += a[i]
        i = i + 1
        return add_recur(rez, i)
    else:    
        return rez

def main():
    """Main entry point for the script."""

    add_for()
    add_while();
    print(add_recur(0,0));

    pass

if __name__ == '__main__':
    sys.exit(main())
