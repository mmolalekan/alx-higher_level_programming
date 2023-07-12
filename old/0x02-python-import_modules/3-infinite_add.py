#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    total = 0
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            total += int(argv[i])
        print(total)
