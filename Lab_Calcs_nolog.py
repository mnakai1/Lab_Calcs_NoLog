import sys

def UV_exposuretimecalc():
	flux = float(input('What is the current reading on the detector? Detector units should be in middle position.\n')) / 100
	fluence = float(input('How much UVA do you want? (in J/m2)?\n'))
	time = fluence / flux
	print('Time (sec):', time)
	print('Time (min):', int(time/60), 'minutes', int(time - int(time/60)*60), 'seconds')

def platecellcount_nonadjusted():
	whatwehavenotadjusted = input('What was the cell count (not adjusted for trypan blue)?\n')
	whatwewant = input('How many total cells do we want in the end per mL?\n')
	finalvol = float(whatwewant) / (float(whatwehavenotadjusted)/2)
	print(finalvol)
	
def platecellcount_adjusted():
	whatwehaveadjusted = input('What was the cell count after trypan blue adjustment per mL?\n')
	whatwewant = input('How many total cells do we want in the end per mL?\n')
	finalvol = float(whatwewant) / float(whatwehaveadjusted)
	print(finalvol)

	
if __name__ == '__main__':
	
	while True:
		
		#Cell plating calculations here
		mainchoice = input('\n"p"\t--->\tCell count calculations for plating.\n"u"\t--->\tUVA time calculation\n\nInput a command: ')
		if mainchoice == 'p' or mainchoice == 'P':
			try:
				plateinput1 = input('Have you adjusted for trypan blue yet? (Type y if Countess is not being used for cell count) y/n: ')
				if plateinput1.lower() == 'y':
					platecellcount_adjusted()
				elif plateinput1.lower() == 'n':
					platecellcount_nonadjusted()
				else:
					print('\nInvalid input, returning to main menu.')
			except TypeError as localerr:
				print('***Unexpected character type, try again. \nError details: ', localerr, 'n')
			except ZeroDivisionError as localerr:
				print('***I\'m not sure how you managed to get this error message. \nError details: ', localerr, 'n')
			except:
				print('***Unexpected error')
		
		elif mainchoice == 'u' or mainchoice == 'U':
			try:
				UV_exposuretimecalc()
			except:
				print('***Unexpected error')
		else:
			print('Invalid input, try again')
		
		#Asks the user if they want to do another calculation or close the program
		exitinput = input('Do another calculation? y/n: ')
		if exitinput.lower() == 'n':
			try:
				break
			except TypeError as localerr:
				print('***Unexpected character type, exiting program. \nError details: ', localerr, '\n')
				break
		else:
			pass
	
	sys.exit()