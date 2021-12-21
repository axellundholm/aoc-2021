

def play_deter_dirac(points, die, board):
	
	nof_rolls = 0

	while True:
		for ind, val in enumerate(points):

			rolls, die = roll_die(die)
			nof_rolls += 3

			board[ind] = (board[ind] + sum(rolls)) % 10
			points[ind] += board[ind] + 1

			if points[ind] >= 1000:
				return min(points) * nof_rolls

def play_quantum_dirac(points, board, q_wins, q_turn=0, q_occ=1):

	global rolls, nof_rolls

	q_points = list(points)
	q_board = list(board)

	if max(q_points) >= 21:
		q_wins[(q_turn + 1) % 2] += q_occ
		return

	for r in range(7):
		q_board[q_turn] = (board[q_turn] + rolls[r]) % 10
		q_points[q_turn] = points[q_turn] + q_board[q_turn] + 1

		play_quantum_dirac(q_points, q_board, q_wins, (q_turn + 1) % 2, nof_rolls[r] * q_occ)	

	return max(q_wins)


def roll_die(die):
	
	rolls = []

	for i in range(3):
		die = die % 100 + 1
		rolls.append(die)

	return rolls, die

def setup_game(l):

	global rolls, nof_rolls
	
	points = [0] * 2
	die = 0
	board = [l[0] - 1, l[1] - 1]

	q_points = [0] * 2
	q_board = list(board)
	q_wins = [0] * 2

	rolls = (3, 4, 5, 6, 7, 8, 9)
	nof_rolls = (1, 3, 6, 7, 6, 3, 1)

	return points, die, board, q_points, q_board, q_wins

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [int(x.strip()[-1]) for x in l]

	points, die, board, q_points, q_board, q_wins = setup_game(l)

	print("Answer to Part One: " + str(play_deter_dirac(points, die, board)))
	print("Answer to Part Two: " + str(play_quantum_dirac(q_points, q_board, q_wins)))


if __name__=="__main__":
	main()


