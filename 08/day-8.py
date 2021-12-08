if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [[[dig for dig in dig.split()] for dig in x.strip().split(' | ')] \
	for x in l]

	filtered_dig = [[num for num in d[1] if len(num) == 2 or len(num) == 3 \
	or len(num) == 4 or len(num) == 7] for d in l]

	sum_dig = sum(len(d) for d in filtered_dig)

	print("Answer to Part One: " + str(sum_dig))
	print("Answer to Part Two: " + str('N/A'))

	# a(7), cf(1), bd(4), g(9), e(8), c(6), f(6)


