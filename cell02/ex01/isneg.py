while(True):
	x = input()
	try:
		x = int(x)
		if (x < 0):
			print("This number is negative.")

		elif (x > 0):
			print("This number is positive.")

		elif (x == 0):
			print("This number is both positive and negative.")

		break
		
	except ValueError:
		break