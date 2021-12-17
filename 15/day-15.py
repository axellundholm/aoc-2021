import numpy as np


def find_low_risk(cave):

	global adj_que, acc_risk, cost_que, tmp_que

	rows = len(cave)
	cols = len(cave[0])

	acc_risk = [['NaN' for i in range(len(cave[0]))] for j in range(len(cave))]
	acc_risk[0][0] = 0

	adj_que = [[0] * 2]
	cost_que = []
	tmp_que = []
	
	while acc_risk[len(acc_risk) - 1][len(acc_risk[0]) - 1] is 'NaN':

		while len(tmp_que) > 0:
			adj_que.append(tmp_que.pop())

		adj_que = find_adj(adj_que, rows, cols) #for now



		while len(cost_que) > 0:
			calc_acc_risk(cost_que.pop(0), cave, acc_risk, rows, cols)

	return acc_risk[rows - 1][cols - 1]

def find_adj(adj_que, rows, cols):

	global acc_risk, cost_que, tmp_que

	adj_loc = []

	for loc in adj_que:
		if loc[0] != rows - 1 and [loc[0] + 1, loc[1]] not in adj_loc: # down
			adj_loc.append([loc[0] + 1, loc[1]]) 

		if loc[1] != cols - 1 and [loc[0], loc[1] + 1] not in adj_loc: # right
			adj_loc.append([loc[0], loc[1] + 1]) 

		if loc[0] != 0 and [loc[0] - 1, loc[1]] not in adj_loc:
			adj_loc.append([loc[0] - 1, loc[1]]) 

		if loc[1] != 0 and [loc[0], loc[1] - 1] not in adj_loc:
			adj_loc.append([loc[0], loc[1] - 1]) 

	for x in adj_loc:
		if acc_risk[x[0]][x[1]] == 'NaN':
			tmp_que.append(x)

	return adj_loc

def calc_acc_risk(loc, cave, acc_risk, rows, cols):

	global adj_que

	cost = 'NaN'

	if loc[0] != 0:
		cost = min(cost, acc_risk[loc[0] - 1][loc[1]])
	if loc[0] != rows - 1:
		cost = min(cost, acc_risk[loc[0] + 1][loc[1]])
	if loc[1] != 0:
		cost = min(cost, acc_risk[loc[0]][loc[1] - 1])
	if loc[1] != cols - 1:
		cost = min(cost, acc_risk[loc[0]][loc[1] + 1])

	if cost + cave[loc[0]][loc[1]] < acc_risk[loc[0]][loc[1]]:
		acc_risk[loc[0]][loc[1]] = cost + cave[loc[0]][loc[1]]
		adj_que.append([loc[0], loc[1]])

def build_large_cave(cave, scale):

	shift_cave = np.array(cave)
	large_cave = np.zeros([len(cave) * scale] * 2, dtype=int)

	for s in range(scale * 2 - 1):
		for r in range(scale):
			for c in range(scale):
				r_ind = r * len(cave)
				c_ind = c * len(cave)
				if r + c == s:
					large_cave[r_ind:r_ind+shift_cave.shape[0], c_ind:c_ind+shift_cave.shape[1]] += shift_cave
		shift_cave = (shift_cave % 9) + 1

	return large_cave.tolist()


if __name__=="__main__":
	f = open('test-input', 'r')
	
	l = f.readlines()
	cave = [[int(i) for i in list(x.strip())] for x in l]

	test = [[1, 2, 3], [3, 4, 5], [5, 6, 9]]
	scale = 5

	large_cave = build_large_cave(cave, scale)

	print("Answer to Part One: " + str(find_low_risk(cave)))
	print("Answer to Part Two: " + str(find_low_risk(large_cave)))


