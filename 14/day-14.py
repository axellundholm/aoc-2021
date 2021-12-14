
def poly_step(pair_map, pair_bin, pair_ins, char_map, char_bin, nof_steps):

	old_pair_bin = list(pair_bin)
	char_bin = list(char_bin)
	
	for n in range(nof_steps):
		new_pair_bin = [0] * len(old_pair_bin)

		for b in range(len(old_pair_bin)):
			new_pair_bin[pair_map.index(pair_ins[b][0])] += old_pair_bin[b]
			new_pair_bin[pair_map.index(pair_ins[b][1])] += old_pair_bin[b]

			char_bin[char_map.index(pair_ins[b][0][1])] += old_pair_bin[b]

		old_pair_bin = list(new_pair_bin)

	return sorted(char_bin)[-1] - sorted(char_bin)[0]

def setup_poly(input):

	tmp_map = [''.join([l[0][p], l[0][p + 1]]) for p in range(len(l[0]) - 1)]

	rules = [x.split(' -> ') for x in l[2:]]

	pair_map = [x[0] for x in rules]
	pair_bin = [0] * len(pair_map)
	for x in tmp_map:
		pair_bin[pair_map.index(x)] = tmp_map.count(x) 

	pair_ins = [[''.join([x[0][0], x[1]]), ''.join([x[1], x[0][1]])] for x in rules]

	char_map = list(set((x[1] for x in rules)))
	char_bin = [0] * len(char_map)
	for x in input[0]:
		char_bin[char_map.index(x)] = input[0].count(x) 

	return pair_map, pair_bin, pair_ins, char_map, char_bin


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	pair_map, pair_bin, pair_ins, char_map, char_bin = setup_poly(l)

	print("Answer to Part One: " + str(poly_step(pair_map, pair_bin, pair_ins, char_map, char_bin, 10)))
	print("Answer to Part Two: " + str(poly_step(pair_map, pair_bin, pair_ins, char_map, char_bin, 40)))


	