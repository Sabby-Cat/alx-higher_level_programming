#!/usr/bin/python3
"""nqueens program prints coordinates of n queens
on nxn grid so all are in non-attacking positions"""


from sys import argv

if __name__ == "__main__":
    ret = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        ret.append([i, None])

    def clear_ret(x):
        """clears answers from point of failure"""
        for i in range(x, n):
            ret[i][1] = None

    def exists(y):
        """check if already exist in y value"""
        for x in range(n):
            if y == ret[x][1]:
                return True
        return False

    def check(x, y):
        """checks if solution is usable"""
        if (exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(ret[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def nqueens(x):
        """recursive backtracking function to find ans"""
        for y in range(n):
            clear_ret(x)
            if check(x, y):
                ret[x][1] = y
                if (x == n - 1):
                    print(ret)
                else:
                    nqueens(x + 1)

    nqueens(0)