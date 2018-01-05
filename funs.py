try:
	from sys import exit
	from os import system
except ImportError as e:
	print("Failed to import 1 or more libraries")
	print(e)
	exit()
def addElements(lst):
		system('cls')
		print("Okay, Lets add things to your list!")
		print("Just keep Entering stuff by Hitting Enter or enter in blank to finish")
		input("Ready, Click Enter")
		entering = True
		while entering:
			e = input("Enter to add to the list or BLANK to finish")
			if e == "" or e == "BLANK" or e =="blank":
				entering = False
			else:
				lst.append(e.lower())
		print(lst)
		return None

def showByElement(lst):
	system('cls')
	ind = int(input("Enter what number Element you want"))
	print("Your Item is:", " ", lst[ind-1])
	return None

def showSlice(lst):
	system('cls')
	print("You Will be asked to enter the element you want to start from and whether you want stuff before or after it.")
	idn = int(input("Enter from which element you want to 'slice from:'"))
	bof = input("Before or After? (B/A)")
	if bof == "B":
		print(lst[:idn-1])
	if bof == "A":
		print(lst[idn-1:])
	return None
def remItem(lst):
	print("Enter what number item you want to remove")
	inp = int(input())
	el = str(lst[inp-1])
	print("Is this the item you want to remove:", " ", el)
	conf = input("Y/n")
	if conf =="n":
		return None
	lst.remove(el)
	print("Item Removed!")
	input()
	return None
def saveToFile(lst, flname):
	print("I will now try to save the current list to the file 'DATA.txt', make sure it is empty!")
	try:
		with open(flname , 'w') as f:
			for i in lst:
				f.write(str(i) + '\n')
	except Exception as e:
		print(e)
		print("write Failed")
		return None
	print("Write succesful!")
	return None
def loadToList(flname):
	finalRes = []
	try:
		print("reading")
		with open(flname) as f:
			lines = f.readlines()
			for item in lines:
				finalRes.append(item.strip())
	except Exception as e:
		print(e)
	return finalRes






