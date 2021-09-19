#!/usr/bin/env python3

def my_var():
	un = 42
	deux = "42"
	trois = "quarante deux"
	quatre = 42.0
	cinq = True
	six = [42]
	sept = {42:42}
	huit = (42,)
	neuf = set()
	print(un, "un est de",type(un))
	print(deux, "deux est de",type(deux))
	print(trois, "trois est de",type(trois))
	print(quatre, "quatre est de",type(quatre))
	print(cinq, "cinq est de",type(cinq))
	print(six , "six est de",type(six))
	print(sept, "sept est de",type(sept))
	print(huit, "huit est de",type(huit))
	print(neuf, "neuf est de",type(neuf))


if __name__ == '__main__':
	my_var()
