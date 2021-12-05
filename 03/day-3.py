
def significant_value(list):
	
	bin_sum = [0] * len(list[0])

	for l in list:
		bin_sum = [int(a) + b for a, b in zip(l, bin_sum)]

	return bin_sum


def power_consumption(list):

	gamma = []
	epsilon = []
	bin_sum = significant_value(list)
	
	for b in bin_sum:
		gamma.append(str(1)) if b > len(list) / 2 else gamma.append(str(0))
		epsilon.append(str(0)) if b > len(list) / 2 else epsilon.append(str(1))

	return(int(''.join(gamma), 2) * int(''.join(epsilon), 2))


def oxygen_generator(list):
	
	for c in range(len(list[0])):
		bin_sum = significant_value(list)

		list = [x for x in list if int(x[c]) is int(bin_sum[c] >= (float(len(list)) / 2))] 
		
		if len(list) == 1:
			return int(''.join(list[0]), 2)

def co2_scrubber(list):
	
	for c in range(len(list[0])):
		bin_sum = significant_value(list)


		list = [x for x in list if int(x[c]) is not int(bin_sum[c] >= (float(len(list)) / 2))] 
		
		if len(list) == 1:
			return int(''.join(list[0]), 2)

def life_support(list):

	return oxygen_generator(list) * co2_scrubber(list)


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [list(x.strip()) for x in l]

	print("Answer to Part One: " + str(power_consumption(l)))
	print("Answer to Part Two: " + str(life_support(l)))
