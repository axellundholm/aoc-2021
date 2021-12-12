
def step_octos(octos):

	flashes = [0] * 3
	sync_flash = False
	step = 1

	
	while True:
		for i in range(len(octos)):
			for j in range(len(octos[0])):
				octos[i][j] += 1

		while True:

			for i in range(len(octos)):
				for j in range(len(octos[0])):
					if octos[i][j] > 9:
						octos[i][j] = 0
						flashes[1] += 1

						adj_i = [x + i for x in [-1, 0, 1] if x + i in range(len(octos))]
						adj_j = [x + j for x in [-1, 0, 1] if x + j in range(len(octos[0]))]

						for n in adj_i:
							for m in adj_j:
								if (i, j) != (n, m) and octos[n][m] > 0:
									octos[n][m] += 1

			if flashes[0] == flashes[1]:
				break

			flashes[0] = flashes[1]

		if step == 100:
			flashes[2] = flashes[0]
		if sum([sum(x) for x in octos]) == 0 and not sync_flash:
			sync_flash = step
			break

		step += 1

	return flashes[2], sync_flash

if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	octos = [[int(n) for n in list(x.strip())] for x in l]

	flashes, sync_flash = step_octos(octos)

	print("Answer to Part One: " + str(flashes))
	print("Answer to Part Two: " + str(sync_flash))

	