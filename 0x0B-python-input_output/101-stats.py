#!/usr/bin/python3
"""calculated log metrics of stdin"""


def my_print(size, stat_cd):
    """prints stats of stdin"""
    print("File size: {}".format(size))
    for key in sorted(stat_cd):
        print("{}: {}".format(key, stat_cd[key]))


if __name__ == "__main__":
    import sys

    size = 0
    num = 0
    stat_cd = {}
    vld_cd = ['200', '301', '400', '401', '403', '404', '405', '500']
    try:
        for line in sys.stdin:
            if num == 10:
                my_print(size, stat_cd)
                num = 1
            else:
                num += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in vld_cd:
                    if stat_cd.get(line[-2], -1) == -1:
                        stat_cd[line[-2]] = 1
                    else:
                        stat_cd[line[-2]] += 1
            except IndexError:
                pass
        my_print(size, stat_cd)
    except KeyboardInterrupt:
        my_print(size, stat_cd)
        raise
