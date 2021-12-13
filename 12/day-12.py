

def find_paths(rough_map, loc, path, revisit):

	global paths, small_cave

	path = list(path)
	
	if loc.islower() and loc in path:
		if loc != revisit:
			return False
		else:
			revisit = False

	path.append(loc)

	if loc == 'end':
		paths.append(','.join(path))
		return True

	possible_paths = sorted([x for x in rough_map if x[0] == loc])

	for x in possible_paths:
		find_paths(rough_map, x[1], path, revisit)


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split('-') for x in l]

	unique_small_caves = []
	[[unique_small_caves.append(c) for c in x if c.islower() and len(c) < 3] for x in l]
	unique_small_caves = sorted(set(unique_small_caves))

	l = sorted(l + [x[::-1] for x in l], key=len)
	rough_map = [x for x in l if x[1] != 'start' and x[0] != 'end']

	paths = []
	for small_cave in unique_small_caves:
		find_paths(rough_map, 'start', [], small_cave)
	revisit_paths = set(paths)
	
	paths = []
	find_paths(rough_map, 'start', [], False)

	print("Answer to Part One: " + str(len(paths)))
	print("Answer to Part Two: " + str(len(revisit_paths)))


	