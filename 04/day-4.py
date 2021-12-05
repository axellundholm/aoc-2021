
def set_up_game(lines):

	global numbers, boards, points, finished
	
	numbers = lines.pop(0).split(',')
	numbers = [int(n) for n in numbers]

	lines = [x.split() for x in lines if x is not '']

	boards = []
	points = []
	finished = []

	for b in range(len(lines) / 5):
		rows = []

		for r in range(5):
			rows.append([int(x) for x in lines.pop(0)])

		boards.append(rows)
		points.append([[0 for i in range(5)] for j in range(2)])

def run_game():

	global numbers, finished

	scores = []

	while len(numbers) is not 0:
		draw_number()

		while len(finished) > 0:
			scores.append(calc_score(finished.pop()))

	return scores[0], scores[-1]

def draw_number():

	global number, numbers, boards, points, finished

	number = numbers.pop(0)

	for b in range(len(boards)):
		for r in range(len(boards[b])):
			for c in range(len(boards[b][r])):
				if boards[b][r][c] is number:
					boards[b][r][c] = False
					points[b][0][r] += 1
					points[b][1][c] += 1
					if points[b][0][r] is 5 or points[b][1][c] is 5:
						finished.append(b)

def calc_score(pos):

	global number, boards, points

	score = 0

	for r in range(len(boards[pos])):
			for c in range(len(boards[pos][r])):
				score += boards[pos][r][c]

	boards.pop(pos)
	points.pop(pos)

	return score * number


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	set_up_game(l)
	nof_boards = len(boards)

	winner, loser = run_game()

	print("Answer to Part One: " + str(winner))
	print("Answer to Part Two: " + str(loser))
