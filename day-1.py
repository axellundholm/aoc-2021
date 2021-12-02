
def count(measurements):

	counter = 0

	for i in range(len(measurements)):
		if measurements[i - 1] < measurements[i]:
			counter += 1

	return counter

def filter_list(measurements):

	filtered_measurements = []

	for i in range(len(measurements) - 1):
		filtered_measurements.append(measurements[i - 1] + measurements[i] + measurements[i + 1])
	
	return filtered_measurements


if __name__=="__main__":
	f = open('input-1.txt', 'r')
	
	l = f.readlines()
	l = [int(x.strip()) for x in l]

	print("Answer to Part One: " + str(count(l)))
	print("Answer to Part Two: " + str(count(filter_list(l))))