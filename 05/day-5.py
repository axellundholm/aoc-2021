



if __name__ == '__main__':
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[[int(axis) for axis in cord.split(',')] for cord in line.strip().split(' -> ')] for line in l]

	maximun = max([max([max(x) for x in list]) for list in l])
	diagram = [[0 for i in range(maximun)] for j in range(maximun)]

	