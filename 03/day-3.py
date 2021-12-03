import numpy as np


def find_gd(list):

	bin_sum = [0] * len(list[0])
	gamma = []
	delta = []

	for l in list:
		bin_sum = [int(a) + b for a, b in zip(l, bin_sum)]

	for b in bin_sum:
		gamma.append(str(1)) if b > len(list) / 2 else gamma.append(str(0))
		delta.append(str(0)) if b > len(list) / 2 else delta.append(str(1))

	return(int(''.join(gamma), 2) * int(''.join(delta), 2))



	pass
if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [list(x.strip()) for x in l]

	print(find_gd(l))

	print("Answer to Part One: " + str(find_gd(l)))
	print("Answer to Part Two: " + str('N/A'))
	