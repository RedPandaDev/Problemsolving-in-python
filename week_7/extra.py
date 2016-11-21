# I’m planning a party to share my love of doughnuts, and have booked a venue that can hold between 1 and 100
# people. Every guest will be given exactly one doughnut when they arrive, whether they want one or not. However,
# I’m very careful with my money, so I want to make sure I don’t have any doughnuts left over. My local bakery sells
# doughnuts in boxes of 6, 9 or 20. Assuming everyone I invite will definitely turn up, which numbers of guests must I
# avoid inviting?
box1 = 6 # 6,12,18,24,30,36,42,48,54,60
box2 = 9 # 9,18,27,36,45,54,63,72,81,90
box3 = 20 # 20,40,60,80,100
good = []
waste=[]


def multiples():
	for i in range(1,101):

		if i % box1 == 0 or i % box2 == 0 or i % box3 == 0:
			good.append(i)
		else:
			waste.append(i)

	return waste

def minusing(waste_list):
	bad = []
	for a in waste_list:

		key = a

		while key > 5:
			if key % 3 == 0 and key != 3:
				good.append(a)
				break
			elif key >= box3:
				key -= box3
			elif key >= box2:
				key -= box2
			elif key >= box1:
				key -= box1

		if key == 0:
			good.append(a)
		else:
			bad.append(a)

	return bad

def minusing2(waste_list):
	bad = []
	for a in waste_list:

		key = a

		while key > 5:
			if key % 3 == 0 and key != 3:
				good.append(a)
				break
			elif key >= box3:
				key -= box3
			elif key >= box1:
				key -= box1
			elif key >= box2:
				key -= box2

		if key == 0:
			good.append(a)
		else:
			bad.append(a)

	return bad

def minusing3(waste_list):
	bad = []
	for a in waste_list:

		key = a

		while key > 5:
			if key % 3 == 0 and key != 3:
				good.append(a)
				break
			elif key >= box2:
				key -= box2
			elif key >= box1:
				key -= box1

		if key == 0:
			good.append(a)
		else:
			bad.append(a)

	return bad

def multiple3(waste_list):
	bad = []
	for a in waste_list:

		key = a

		if key % 3 == 0 and key != 3:
			good.append(a)
		else:
			bad.append(a)

	return bad



def doughnuts(guests = 100):

		# if i - box1 < 0:
		# 	waste.append(i) 
		# elif i != box1 and i-box2 < 0:
		# 	 waste.append(i) 

	return 	multiple3(minusing3(minusing2(minusing(multiples()))))


def calculus():
	import itertools
	numbers = [6,9,20]
	result = [seq for i in range(1,101) for seq in itertools.combinations(numbers, i)]
	return result