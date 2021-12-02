
def calc_pos(list):

	hor = 0
	dep = 0

	for l in list:
		if l[0] == 'forward':
				hor += int(l[1])
		elif l[0] == 'up':
				dep -= int(l[1])
		elif l[0] == 'down':
				dep += int(l[1])

	return(hor*dep)

def calc_pos_mod(list):

	hor = 0
	dep = 0
	aim = 0

	for l in list:
		if l[0] == 'forward':
				hor += int(l[1])
				dep += int(l[1]) * aim
		elif l[0] == 'up':
				aim -= int(l[1])
		elif l[0] == 'down':
				aim += int(l[1])

	return(hor*dep)

	pass


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split() for x in l]

	print("Answer to Part One: " + str(calc_pos(l)))
	print("Answer to Part Two: " + str(calc_pos_mod(l)))