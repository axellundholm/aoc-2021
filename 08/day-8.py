

def sum_unique_num(l):

	filtered_dig = [[num for num in d[1] if len(num) == 2 or len(num) == 3 \
	or len(num) == 4 or len(num) == 7] for d in l]

	return sum(len(d) for d in filtered_dig)

def signal_mapping(input_line):

	sorted_input = [sorted(list(x)) for x in sorted(input_line, key=len)]

	cf = sorted_input.pop(0)

	a = sorted_input.pop(0)
	[a.remove(x) for x in cf]

	bd = sorted_input.pop(0)
	[bd.remove(x) for x in cf]

	eg = sorted_input.pop()
	[eg.remove(x) for x in a+cf+bd]

	b = list([b for b in sorted_input[-3:] if not (bd[0] in b and bd[1] in b)][0])
	[b.remove(x) for x in a+cf+eg]

	d = list(bd)
	[d.remove(x) for x in b]

	f = list([f for f in sorted_input[-3:] if not (cf[0] in f and cf[1] in f)][0])
	[f.remove(x) for x in a+bd+eg]

	c = list(cf)
	[c.remove(x) for x in f]

	g = list([g for g in sorted_input[-3:] if not (eg[0] in g and eg[1] in g)][0])
	[g.remove(x) for x in a+bd+cf]

	e = list(eg)
	[e.remove(x) for x in g]

	zero = sorted([a + b + c + e + f + g][0])
	one = sorted([c + f][0])
	two = sorted([a + c + d + e + g][0])
	three = sorted([a + c + d + f + g][0])
	four = sorted([b + c + d + f][0])
	five = sorted([a + b + d + f + g][0])
	six = sorted([a + b + d + e + f + g][0])
	seven = sorted([a + c + f][0])
	eight = sorted([a + b + c + d + e + f + g][0])
	nine = sorted([a + b + c + d + f + g][0])
	
	signal_map = [zero, one, two, three, four, five, six, seven, eight, nine]

	return signal_map

def find_output_value(line):

	signal_map = signal_mapping(line[0])
	sorted_output = [sorted(list(x)) for x in line[1]]

	output_val = int(''.join([str(signal_map.index(x)) for x in sorted_output]))

	return output_val

	
if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[[dig for dig in dig.split()] for dig in x.strip().split(' | ')] \
	for x in l]

	sum_output_vals = sum([find_output_value(x) for x in l])

	print("Answer to Part One: " + str(sum_unique_num(l)))
	print("Answer to Part Two: " + str(sum_output_vals))


