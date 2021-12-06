

def take_step(inst, diagonal):

	global diagram

	x1 = inst[0][0]
	x2 = inst[1][0]
	y1 = inst[0][1]
	y2 = inst[1][1]

	if y1 == y2:
		x = x1
		for i in range(abs(x1 - x2) + 1):
			diagram[y1][x] += 1
			x += ((x2 - x1) / abs(x2 - x1))
	elif x1 == x2:
		y = y1
		for i in range(abs(y1 - y2) + 1):
			diagram[y][x1] += 1
			y += ((y2 - y1) / abs(y2 - y1))
	else:
		if not diagonal:
			return
		x = x1
		y = y1
		for i in range(abs(x1 - x2) + 1):
			diagram[y][x] += 1
			x += ((x2 - x1) / abs(x2 - x1))
			y += ((y2 - y1) / abs(y2 - y1))

def count_intersects():

	global diagram

	intersects = 0

	for i in diagram:
		for j in i:
			if j > 1:
				intersects += 1

	return intersects

def calc_hydro_vents(diagonal):

	global l, maximun, diagram

	diagram = [[0 for i in range(maximun)] for j in range(maximun)]

	for inst in l:
		take_step(inst, diagonal)

	return count_intersects()


if __name__ == '__main__':
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[[int(axis) for axis in cord.split(',')] for cord in line.strip().split(' -> ')] for line in l]

	maximun = max([max([max(x) for x in list]) for list in l]) + 1

	print("Answer to Part One: " + str(calc_hydro_vents(False)))
	print("Answer to Part Two: " + str(calc_hydro_vents(True)))




