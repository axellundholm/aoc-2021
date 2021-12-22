import numpy as np

def init_proc(reboot_steps):

	init_region = np.zeros([101, 101, 101])
	
	for step in reboot_steps:

		inst = step[0]
		cube = step[1]
		x = np.array([max(cube[0][0], -50), min(cube[0][1], 50)]) + 50
		y = np.array([max(cube[1][0], -50), min(cube[1][1], 50)]) + 50
		z = np.array([max(cube[2][0], -50), min(cube[2][1], 50)]) + 50

		init_region[x[0]:x[1] + 1, y[0]:y[1] + 1, z[0]:z[1] + 1] = inst

	return int(sum(sum(sum(init_region))))

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	reboot_steps = [x.strip().split(' ') for x in l]
	reboot_steps = [[1, x[1]] if x[0] == 'on' else [0, x[1]] for x in reboot_steps]
	reboot_steps = [[x[0], x[1].split(',')] for x in reboot_steps]
	reboot_steps = [[x[0], [[int(v) for v in c[2:].split('..')] for c in x[1]]] for x in reboot_steps]

	turned_on = init_proc(reboot_steps)

	print("Answer to Part One: " + str(turned_on))
	print("Answer to Part Two: " + str('N/A'))


if __name__=="__main__":
	main()


