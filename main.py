try:
	from sys import exit
	from os import system
except ImportError as e:
	print("Failed to import 1 or more libraries")
	print(e)
	exit()
try:
	import funs
except ImportError as e:
	print("I failed to import the configuration File (I REALL need it!)")
	pritn("Make sure there is a config.py and is in this directory!")


LIST = []

def basicLists():
	global LIST
	if LIST == []:
		print("You don't have anything in your list, Let's get you started and add Stuff!")
		print("NOTE: if you want to load from file just keep pressing enter to enter the menu")
		input("Hit enter to start!")
		funs.addElements(LIST)
	while True:
		system('cls')
		print("Here is your current List" + " ", LIST)
		print("What do you want to do?")
		print("############################")
		print("#1.Show by element         #")
		print("#2.Show a slice            #")
		print("#3.Remove an Item          #")
		print("#4.Save your list to file  #")
		print("#5.Load your list from file#")
		print("#6.Exit to menu            #")
		print("############################")
		choice = int(input())
		if choice == 1:
			funs.showByElement(LIST)
		if choice == 2:
			funs.showSlice(LIST)
		if choice == 3:
			funs.remItem(LIST)
		if choice == 4:
			funs.saveToFile(LIST)
		if choice == 5:
			try:
				LIST = funs.loadFile()
			except Exception as e:
				print("Error occured List not changed")
				print(e)
			print("List updated!")
			input()
		if choice == 6:
			return None

		input("")
while True:
	system('cls')
	print("##################")
	print("#1. Basic Lists  #")
	print("#2. Quit         #")
	print("##################")
	try:
		choice = int(input("What do you want to do"))
		if choice == 1:
			basicLists()
		elif choice == 2:
			exit()
	except ValueError:
		system('cls')
		print("What you entered doesn't look like a valid option;)")
		print("Hit Enter and please try Again!")
		input()