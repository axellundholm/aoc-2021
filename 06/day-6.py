
def step_forward(fish, nof_days):
	
	for d in range(nof_days):
		for f in range(len(fish)):
			if fish[f] > 0:
				fish[f] -= 1
			elif fish[f] == 0:
				fish[f] = 6
				fish.append(8)

	return len(fish)

# def step_backward(fish):
	
# 	for x in range(25):
# 		nof_new_fish = 0

# 		for f in fish:
# 			if f == 8:
# 				nof_new_fish += 1

# 		fish = [f for f in fish if f != 8]

# 		for f in range(len(fish)):
# 			if fish[f] == 6 and nof_new_fish > 0:
# 				fish[f] = 0
# 				nof_new_fish -= 1
# 			else:
# 				fish[f] += 1

# 		print(fish)



if __name__=="__main__":
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip().split(',') for x in l]
	fish_list = [int(n) for n in l[0]]

	# step_backward(fish_list)
	print("Answer to Part One: " + str(step_forward(fish_list, 80)))
	print("Answer to Part Two: " + str('N/A'))