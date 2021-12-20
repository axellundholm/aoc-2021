import numpy as np

def setup_imgage(l):
	alg = l.pop(0)

	img = l[1:]

	img = np.zeros([len(l[1:]), len(l[1:][0])])
	for r, row in enumerate(l[1:]):
		for c, val in enumerate(row):
			img[r, c] = 1 if val == '#' else 0

	img = np.pad(img, 3)

	return alg, img

def enhance(alg, img):
	new_img = np.zeros([len(img) - 2, len(img[0]) - 2])

	for r, row in enumerate(new_img):
		r_old = r + 1
		for c, val in enumerate(row):
			c_old = c + 1

			bin_code = ''

			for y in range(r_old - 1, r_old + 2):
				for x in range(c_old - 1, c_old + 2):
					bin_code += str(int(img[y][x]))

			new_img[r, c] = 1 if alg[int(bin_code, 2)] == '#' else 0

	return np.pad(new_img, 3, mode='edge')

def main():
	f = open('input', 'r')
	
	l = f.readlines()
	l = [x.strip() for x in l]

	alg, img = setup_imgage(l)

	for x in range(2):
		img = enhance(alg, img)

	pixels_2 = int(sum(sum(img)))

	for x in range(48):
		img = enhance(alg, img)

	pixels_50 = int(sum(sum(img)))

	print("Answer to Part One: " + str(pixels_2))
	print("Answer to Part Two: " + str(pixels_50))


if __name__=="__main__":
	main()


