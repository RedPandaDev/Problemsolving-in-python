######### 1 #########


# def counting(i):
# 	print(i)
# 	i -= 1
# 	if i == 0: return
# 	counting(i)

def counting(i):
	print(i)
	i *=2
	if i > 1024: return
	counting(i)


######## 3 #########
def printList(a):
	while len(a) > 0:
		print(a.pop(0))
	#### Doesn't print twice as 'pop' removes the items from the list


######## 4 ########
#import csv

# with open('facup.csv') as csvfile:
# 	rdr = csv.reader(csvfile)
# 	for row in rdr:
# 		print(row[0] + " last won in " + row[1])
# 		print(type(row[1])) ### year is entered as string so integer operations would not work

# 		year = int(row[1])
# 		if year % 2 == 0:
# 			print(True)
# 		else:
# 			print(False)

######## 5 ########

import csv
def winners():
	with open('MultipleTourWinners.csv') as csvfile:
		rdr = csv.reader(csvfile)
		for row in rdr:

			if row[1] == "FRA":
				print(row[0] + ", "+ row[2])



####### 6 ########

def iterate():
	for n in range(0,101,2):
		print(n)

####### 7 #######

def enu_winners():
	with open('MultipleTourWinners.csv') as csvfile:
		rdr = csv.reader(csvfile)

		for i, wins in enumerate(rdr):
			if int(wins[2]) >= 3:
				print(i, "with", wins[2], "wins.")

######## 8 ######
def mark():
	mark = int(input("Enter mark: "))
	if mark <= 50 or mark > 60:
	# Mark can't be both lower than 50 and higher than 60, 
	# 'and' changed to 'or' - semantic
	# Mark is taken as string but used as int - runtime
		print("Result is 2:2")

	# Print the first 10 square numbers
	for n in range (1,11): # range can't be from higher to lower, swaped places - semantic
		print(n * n)

def f(n):
	if n == 1 or n == 2: #### n = 1, needs == instead - syntax
		return 1
	else: ##### Mising double colon - syntax
		return f(n-1) + f(n-2)