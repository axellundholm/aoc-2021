
def simulate_fish(fish, nof_days):

	fish = list(fish)
	
	for d in range(nof_days):
		new_fish = fish.pop(0)

		fish[6] += new_fish
		fish.append(new_fish)

	sum = 0
	for f in fish:
		sum += f
	return sum


if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split(',') for x in l]
	l = [int(n) for n in l[0]]

	fish = 9 * [0]
	for f in l:
		fish[f] += 1

	print("Answer to Part One: " + str(simulate_fish(fish, 80)))
	print("Answer to Part Two: " + str(simulate_fish(fish, 256)))