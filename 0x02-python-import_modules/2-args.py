#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv) - 1
    print("{} {}".format(ac, "argument" if ac == 1 else "arguments"), end="")
    print("{}".format("." if ac == 0 else ":"))
    for i in range(1, ac + 1):
        print("{}: {}".format(i, sys.argv[i]))
