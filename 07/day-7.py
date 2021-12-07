
def calc_fuel(subs, ref, triangluar):
	fuel = [0] * len(subs)

	for s in range(len(subs)):
		if triangluar:
			fuel[s] = (abs(ref - subs[s]) * (abs(ref - subs[s]) + 1)) / 2
		else:
			fuel[s] = abs(ref - subs[s])

	return sum(fuel)


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split(',') for x in l]
	l = [int(n) for n in l[0]]

	fuel_normal = min([calc_fuel(l, i, False) for i in range(min(l), max(l))])
	fuel_triangular = min([calc_fuel(l, i, True) for i in range(min(l), max(l))])

	print("Answer to Part One: " + str(fuel_normal))
	print("Answer to Part Two: " + str(fuel_triangular))
