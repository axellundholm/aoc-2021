
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
	vel_x_max = x_tgt[-1]
	vel_y_min = y_tgt[0]

	max_hit_y = 0
	nof_hits = 0

	for x in range(vel_x_max + 1):
		for y in range(vel_y_min, -vel_y_min):
			y_max = fire_probe([x, y], x_tgt, y_tgt)
			if y_max is not False:
				max_hit_y = max(y_max, max_hit_y)
				nof_hits += 1

	print("Answer to Part One: " + str(max_hit_y))
	print("Answer to Part Two: " + str(nof_hits))


