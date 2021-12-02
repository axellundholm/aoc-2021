
def count(measurements):

	counter = 0

	for i in range(len(measurements)):
		if measurements[i - 1] < measurements[i]:
			counter += 1

	return counter


if __name__=="__main__":
	f = open('input-1.txt', 'r')
	
	l = f.readlines()
	l = [int(x.strip()) for x in l]

	print("Answer to Part One: " + str(count(l)))