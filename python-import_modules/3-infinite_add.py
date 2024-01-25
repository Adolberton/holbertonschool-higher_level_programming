#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    args = sys.argv
    for i in range(1, len(sys.argv)):
        result += int(args[i])
    print(result)
