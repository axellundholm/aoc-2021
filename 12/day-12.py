

def find_paths(rough_map, loc, twice, path):

	global connections, small_cave

	path = list(path)
	path.append(loc)

	remaining_connections = sorted(list(rough_map))

	if loc == 'end':
		# print(','.join(path))
		return True

	if loc.islower() and not (twice and loc == small_cave) :
		remaining_connections = [x for x in remaining_connections if x[1] != loc]
	else:
		twice = False

	possible_paths = [x for x in remaining_connections if x[0] == loc]

	for x in possible_paths:
		if find_paths([rc for rc in remaining_connections if rc != x], x[1], twice, path):
			connections += 1


		
	


if __name__=="__main__":
	f = open('test-input-1', 'r')
	
	l = f.readlines()
	l = [x.strip().split('-') for x in l]

	unique_small_caves = []
	[[unique_small_caves.append(c) for c in x if c.islower() and len(c) < 3] for x in l]
	unique_small_caves = sorted(set(unique_small_caves))

	l = sorted(l + [x[::-1] for x in l], key=len)
	rough_map = [x for x in l if x[1] != 'start' and x[0] != 'end']

	connections = 0

	for small_cave in unique_small_caves:
		find_paths(rough_map, 'start', True, [])

	
	# connections = 0
	# find_paths(rough_map, 'start', False, [])


	print("Answer to Part One: " + str(connections))
	print("Answer to Part Two: " + str('N/A'))