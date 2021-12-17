
def fire_probe(vel, x_tgt, y_tgt):
	
	pos = [0] * 2
	y_max = 0

	while pos[0] <= x_tgt[-1] + 1 and pos[1] >= y_tgt[0] - 1:

		pos[0] += vel[0]
		pos[1] += vel[1]

		vel[0] -= int(vel[0] > 0)
		vel[1] -= 1

		y_max = max(y_max, pos[1])

		if pos[0] in x_tgt and pos[1] in y_tgt:
			return y_max

	return False


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip()[13:] for x in l][0].split(', ')

	l = [[int(y) for y in x[2:].split('..')] for x in l]

	x_tgt = range(l[0][0], l[0][1] + 1)
	y_tgt = range(l[1][0], l[1][1] + 1)

	x_min, x_max = x_tgt[0], x_tgt[-1]
	y_min, y_max = y_tgt[0], y_tgt[-1]

	y_max_max = 0
	hits = 0

	for x in range(x_max + 1):
		for y in range(y_min, -y_min):
			y_max = fire_probe([x, y], x_tgt, y_tgt)
			if y_max is not False:
				y_max_max = max(y_max, y_max_max)
				hits += 1

	print("Answer to Part One: " + str(y_max_max))
	print("Answer to Part Two: " + str(hits))


