

def set_up_game(lines):
	numbers = lines.pop(0).split(',')
	numbers = [int(n) for n in numbers]

	lines = [x.split() for x in lines if x is not '']

	boards = []
	points = []

	for b in range(len(l) / 5):
		rows = []

		for r in range(5):
			rows.append([int(x) for x in lines.pop(0)])

		boards.append(rows)

		points.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

	return numbers, boards, points

def print_boards(boards, points):

	for b in range(len(boards)):
		print('Board number: ' + str(b + 1))
		for r in boards[b]:
			print(r)
		print points[b]
	print('')

def draw_number(numbers, boards, points):
	number = numbers.pop(0)

	for b in range(len(boards)):
		for r in range(len(boards[b])):
			for c in range(len(boards[b][r])):
				if boards[b][r][c] is number:
					boards[b][r][c] = False
					points[b][0][r] += 1
					points[b][1][c] += 1

	return numbers, boards, points

def check_points(numbers, boards, points):

	for b in range(len(points)):
		for r in range(len(points[b])):
			for c in range(len(points[b][r])):
				if points[b][r][c] == 5:
					return 1

	return 0


if __name__=="__main__":
	f = open('test-input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	numbers, boards, points = set_up_game(l)

	round = 1
	winner = 0

	while len(numbers) is not 0 and winner is 0:
		numbers, boards, points = draw_number(numbers, boards, points)
		winner = check_points(numbers, boards, points)
		round += 1

	print("Answer to Part One: " + str('N/A'))
	print("Answer to Part Two: " + str('N/A'))