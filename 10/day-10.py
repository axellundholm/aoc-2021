

def check_illegal(line):

	l = list(line)

	opening = ['(', '[', '{', '<']
	closing = [')', ']', '}', '>']
	p_tbl_1 = [3, 57, 1197, 25137]
	p_tbl_2 = [1, 2, 3, 4]

	points = [0] * 2

	stack = []

	while len(l) > 0:
		if l[0] in closing:
			if closing.index(l[0]) == opening.index(stack[-1]):
				stack.pop()
				l.pop(0)
			else:
				points[0] = p_tbl_1[closing.index(l[0])]
				return points
		else:
			stack.append(l.pop(0))

	stack.reverse()

	for x in stack:
		points[1] = points[1] * 5 + p_tbl_2[opening.index(x)]
	return points


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	points = [check_illegal(x) for x in l]
	corrupt_points = sum([p[0] for p in points])
	incomplete_points = sorted([p[1] for p in points if p[1] > 0])
	incomplete_points = incomplete_points[len(incomplete_points) / 2]

	print("Answer to Part One: " + str(corrupt_points))
	print("Answer to Part Two: " + str(incomplete_points))
