
def fold_paper(dots, folds):

	first_fold = True

	for f in folds:
		if f[0] == 'y':
			dots = [(d[0], d[1] - int(d[1] > f[1]) * (d[1] - f[1]) * 2) for d in dots]
		elif f[0] == 'x':
			dots = [(d[0] - int(d[0] > f[1]) * (d[0] - f[1]) * 2, d[1]) for d in dots]
		if first_fold:
			nof_dots = len(set(dots))
			first_fold = False

	x_max= max([d[0] for d in dots])
	y_max= max([d[1] for d in dots])

	dot_matrix = [['.' for i in range(y_max + 1)] for j in range(x_max + 1)]

	for d in dots:
		dot_matrix[d[0]][d[1]] = '#'

	for x in range(len(dot_matrix)):
		dot_matrix[x] = ''.join(dot_matrix[x])

	return nof_dots, dot_matrix


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	dots = [x.split(',') for x in l if len(x) > 0 and 'fold' not in x]
	dots = [[int(x) for x in d] for d in dots]

	folds = [x[11:].split('=') for x in l if 'fold' in x]
	folds = [[x[0], int(x[1])] for x in folds]

	nof_dots, dot_matrix = fold_paper(dots, folds)

	print("Answer to Part One: " + str(nof_dots))
	print("Answer to Part Two:")

	for x in range(len(dot_matrix)):
		print(dot_matrix[x])


		