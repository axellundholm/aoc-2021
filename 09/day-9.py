
def check_adj_loc(r_ind, c_ind):

	global heightmap, rows, cols

	if r_ind != 0:
		if heightmap[r_ind][c_ind] >= heightmap[r_ind - 1][c_ind]:
			return False
	if r_ind != rows - 1:
		if heightmap[r_ind][c_ind] >= heightmap[r_ind + 1][c_ind]:
			return False
	if c_ind != 0:
		if heightmap[r_ind][c_ind] >= heightmap[r_ind][c_ind - 1]:
			return False
	if c_ind != cols - 1:
		if heightmap[r_ind][c_ind] >= heightmap[r_ind][c_ind + 1]:
			return False

	return True

def find_low_points():

	global rows, cols

	low_points = []

	for r_ind in range(rows):
		for c_ind in range(cols):
			if check_adj_loc(r_ind, c_ind):
				low_points.append(heightmap[r_ind][c_ind])

	return sum([x + 1 for x in low_points])

def find_basins():

	global basins

	basins = [[]]
	basin_number = 0
	
	for r_ind in range(rows):
		for c_ind in range(cols):
			if is_basin(r_ind, c_ind, basin_number) == False:
				basin_number += 1
				basins.append([])

	basins = [len(x) for x in basins if len(x) > 0]

	res = 1

	for b in sorted(basins)[-3:]:
		res = res * b
	return res

def is_basin(r_ind, c_ind, basin_number):

	global basins

	if heightmap[r_ind][c_ind] == 9 or heightmap[r_ind][c_ind] == -1:
		return False

	basins[basin_number].append((r_ind, c_ind))
	heightmap[r_ind][c_ind] = -1

	if r_ind != 0:
		is_basin(r_ind - 1, c_ind, basin_number)
	if r_ind != rows - 1:
		is_basin(r_ind + 1, c_ind, basin_number)
	if c_ind != 0:
		is_basin(r_ind, c_ind - 1, basin_number)
	if c_ind != cols - 1:
		is_basin(r_ind, c_ind + 1, basin_number)


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	heightmap = [[int(n) for n in list(x.strip())] for x in l]

	rows = len(heightmap)
	cols = len(heightmap[0])

	print("Answer to Part One: " + str(find_low_points()))
	print("Answer to Part Two: " + str(find_basins()))





				
				