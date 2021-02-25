def sequence(num):
	first = 0
	second = 1
	temp = 0
	
	for i in range (0, num):
		temp = second
		second = first + second
		first = temp
		
	return second
	
