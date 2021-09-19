#!/usr/bin/env python3
# -*-coding:utf-8 -*-

def geohashing():
    import sys
    if (len(sys.argv) != 4):
        print("""usage: latitude longitude precision date sous cette forme avec
        lheure-minute-seconde convertie en seconde   2005-05-26-10458.68""")
        sys.exit(0)

    antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())

if __name__ == '__main__':
    geohashing()
