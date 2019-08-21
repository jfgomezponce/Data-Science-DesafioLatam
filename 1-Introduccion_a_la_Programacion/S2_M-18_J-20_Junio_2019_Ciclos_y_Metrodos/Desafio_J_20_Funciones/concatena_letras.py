import sys
import string

def gen(num):
	# print(string.ascii_lowercase[:num])
	return string.ascii_lowercase[:num]
letras_concatenadas = gen(int(input()))
#gen(int(sys.argv[1]))