try:
	from sys import exit
	from os import system
	from getpass import getpass
	import os.path
except ImportError as e:
	print("Failed to import 1 or more libraries")
	print(e)
	exit()
try:
	import funs
except ImportError as e:
	print("I failed to import the Function File (I REALL need it!)")
	prinn("Make sure there is a funs.py and is in this directory!")

def hackProof():
	def openFile():
		try:
			cred =funs.loadToList("Cred.txt")
		except Exception as e:
			print("I failed to load secret.txt make sure it exists")
			return None
		userName = cred[0]
		passwd = cred[1]

		username = input("Enter your username")
		password = getpass(prompt='nput your password')

		if username == userName and passwd == password:
			print("Opening File!")
			system('secret.txt')
		else:
			print("Incorrect Credentials")
		input()
	def genCred():
		print("Okay it looks like you have not set your password yet so lets do that shall we?")
		userName = input("Enter your username that you want to use:")
#		print(funs.suggestedPass())
		ready = False
		while ready == False:
			newPass = getpass(prompt='Please Enter the new password')
			newPass1 = getpass(prompt='Please Enter the new password again')
			if funs.valPass(newPass) == True:	
				if newPass != newPass1:
					print("The passwords don't match. Please try again")
				else:
					with open('secret.txt', 'w+') as f:
						f.write("This is your secret file get rid of this line and add whatever you want!")
					ready = True

			else:
				print("Password not valid Make sure there a is small and capital letter and atleast 1 number!")
		
		with open('Cred.txt', 'w+') as f:
			f.write(userName + '\n')
			f.write(newPass + '\n')
		return None
	if os.path.exists('Cred.txt') == False:
		print("File does not exist")
		genCred()
	while True:
		print("########################")
		print("#1. Open file          #")
		print("#2. Return To menu     #")
		print("########################")
		choice = int(input("What do you want to do?"))

		if choice == 1:
			openFile()
		if choice == 2:
			return None
def list_MinMax():
	LIST = []
	maxVal = int(input("Enter the maximum value for your list"))
	minVal = int(input("Enter the minimim value for your list"))
	def loadAndCheck():
		global LIST
		tmpList = []
		result = funs.loadToList("minMax.txt")
		result = [int(i) for i in result]

		for val in result:
			if val > minVal and val < maxVal:
				tmpList.append(val)
				print("Number {} is in bound and added succesfully".format(val))
			else:
				print("Number {} is not in bound and is skipped".format(val))
		try:
			
			print("Loading Succesful")
			return tmpList
		except Exception as e:
			print("Loading Failed.")
			print("Error: {}".format(e))
	def addVals():
		print("How many numbers do you want to add")
		ite = int(input())
		for i in range(ite):
			
			val = int(input("Enter a number"))

			if val > minVal and val < maxVal:
				LIST.append(val)
				print("Current Highest Value is {} and the lowest is {}".format(max(LIST), min(LIST)))
			else:
				print("Numeber is out of bound")
				print("Remember you said that it can not be smaller than {} and not bigger than {}".format(minVal, maxVal))
		return 
	while True:
		if LIST == []:
			print("It looks like you don't have any values in your list")
			print("To add numbers manually type 'y' or to load from a file just hit enter")
			choice = input()
			if choice == "y":
				addVals()
		
		print("Your current List: {}".format(LIST))
		print("#####################")
		print("#1. Add values      #")
		print("#2. Save to File    #")
		print("#3. Load from file  #")
		print("#4. Return to menu  #")
		print("#####################")

		choice = int(input())
		
		if choice == 1:
			addVals()
		if choice == 2:
			print("Saving to file minMax.txt!")
			funs.saveToFile(LIST, "minMax.txt")
		if choice == 3:
			LIST = loadAndCheck()
		if choice == 4:
			return None

def stringCounter():
	system('cls')
	print("Make sure there is a file called strings.txt and then hit enter")
	input()
	strings = funs.loadToList("strings.txt")

	indwords = 0
	sentences = 0
	for string in strings:
		sentences +=1
		words = string.split()
		length = len(words)
		indwords += length
		print("\n '{}' has {} words".format(string, length))
	
	print("\n Summary:")
	print("Total number of sentences: {}".format(sentences))
	print("Total number of words: {}".format(indwords))
	input()
	return None

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
			funs.saveToFile(LIST, "DATA.txt")
		if choice == 5:
			try:
				LIST = funs.loadToList("DATA.txt")
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
	print("###################")
	print("#1. Basic Lists   #")
	print("#2. String Counter#")
	print("#3. Min and Max   #")
	print("#4. Acces file    #")
	print("#5. Quit          #")
	print("###################")
	# try:
	choice = int(input("What do you want to do"))
	if choice == 1:
		basicLists()
	if choice == 2:
		stringCounter()
	if choice == 3:
		list_MinMax()
	if choice == 4:
		hackProof()
	elif choice == 5:
		exit()
	# except ValueError:
	# 	system('cls')
	# 	print("What you entered doesn't look like a valid option;)")
	# 	print("Hit Enter and please try Again!")
	# 	input()