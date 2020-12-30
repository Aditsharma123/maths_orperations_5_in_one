def orperation_system():
	value1 = float(input('Enter your first value: '))
	value2 = float(input('Enter your second value: '))
	answer1 = value1 + value2
	answer2 = value1 - value2
	answer3 = value1 * value2
	answer4 = value1 / value2
	yn = value1 / value2 * 100
	print('after adding: ', answer1)
	print('after subtracting: ', answer2)
	print('after dividing: ', answer3)
	print('after multiplying: ', answer4)
	print('percentage', yn)
	ll = input('done?: ')
	if ll == 'yes':
		exit()
	else:
		orperation_system()

orperation_system()
