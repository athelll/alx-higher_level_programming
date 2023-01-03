if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    sum = 0    
    for i, args in enumerate(argv):
        sum += int(argv[i])
    print(sum)
