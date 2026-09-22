while(True):
	x = input()
	try:
		x = int(x)
		break

	except ValueError:
		break
if (int(x) == 0):
   	 print("This number is equal to zero.")

else:
    print("This number is different from zero.")
