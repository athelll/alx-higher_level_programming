#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    sum = 0
    for i in range(0, len(argv)):
        sum += int(argv[i])
    print("{:d}".format(sum))
