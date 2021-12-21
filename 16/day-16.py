import math

def parse(package, ver_sum=0, ind=0):

	pkg_ver = int(package[ind:ind + 3], 2)
	pkg_typ = int(package[ind + 3:ind + 6], 2)
	ind += 6

	ver_sum += pkg_ver

	if pkg_typ == 4:
		lit_val = ''

		while True:
			lit_val += package[ind + 1:ind + 5]
			ind += 5

			if package[ind - 5] == '0':
				break

		return ind, ver_sum, int(lit_val, 2)

	else:
		stack = []
		len_typ = int(package[ind])
		ind += 1

		if len_typ == 0:
			sub_len = int(package[ind:ind + 15], 2)
			ind += 15
			old_ind = ind

			while ind < old_ind + sub_len:
				ind, ver_sum, value = parse(package, ver_sum, ind)
				stack.append(value)

		elif len_typ == 1:
			sub_no = int(package[ind:ind + 11], 2)
			ind += 11

			for i in range(sub_no):
				ind, ver_sum, value = parse(package, ver_sum, ind)
				stack.append(value)

		if pkg_typ == 0:
			value = sum(stack)
		elif pkg_typ == 1:
			value = math.prod(stack)
		elif pkg_typ == 2:
			value = min(stack)
		elif pkg_typ == 3:
			value = max(stack)
		elif pkg_typ == 5:
			value = int(stack[0] > stack[1])
		elif pkg_typ == 6:
			value = int(stack[0] < stack[1])
		elif pkg_typ == 7:
			value = int(stack[0] == stack[1])

	return ind, ver_sum, value

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l][0]

	binary = bin(int(l, base=16))[2:].zfill(4 * len(l))

	_, ver_sum, value = parse(binary)

	print("Answer to Part One: " + str(ver_sum))
	print("Answer to Part Two: " + str(value))


if __name__=="__main__":
	main()

