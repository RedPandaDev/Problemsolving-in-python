# sports_list = ["football", "rugby", "hockey", "tennis"]

# print(sports_list[0],sports_list[3])
# sports_list.append("cycling")
# list_length = len(sports_list)
# print(list_length)

# i = 0
# while i != list_length:
# 	print(sports_list[i][:1])
# 	i+=1

# sports_list.remove("football")

# length = len(sports_list)
# middle1 = (len(sports_list) // 2) - 1
# middle2 = (len(sports_list) // 2) + 1
# new_list = [sports_list[middle1], sports_list[middle2]]
# print(new_list)
# print(sports_list)

#6

# while i != 10:
# 	print("*", end="")
# 	i+=1
# 	while b != 10:
# 		print()
# 		b += 1
# 		i = 0

# while b != 10:
# 	print()
# 	b += 1
# 	i = 0
# 	while i != 10:
# 		print("*", end="")
# 		i+=1

# 8
def input_sides():
	print("Please enter the length: ")
	m = int(input())
	print("Please enter the width: ")
	n = int(input())
	
	return rectangle(m, n)

def rectangle(m, n):
	i = 0
	b = 0

	while b != m:
		print()
		b += 1
		i = 0
		while i != n:
			print("*", end="")
			i+=1
	return


def weight_limit(limit=3000, max_weight = True):
	weights = [750, 387, 291, 712, 100, 622, 109, 750, 282, 21, 50,67, 10, 120, 235, 420,  510, 311,196]
	load = 0
	i = 0
	add = 0
	reject_list = []
	while i != len(weights):
		add = sorted(weights, reverse = max_weight)[i]
		load += add
		if load > limit:
			load -=add
			reject_list.append(add)
		else:
			print(add)
		i+= 1
	reject_load = sum(reject_list)

	print("Pallets left:", reject_list)
	print("Total weight left:",reject_load)
	print("Total load:", end="")
	return load

# A = {1,2,3,4}
# B = {3,4,5,6}
# >>> A|B
# {1, 2, 3, 4, 5, 6}
# >>> A & B
# {3, 4}
# >>> A - B
# {1, 2}
# >>> (A - B) | (B - A)
# {1, 2, 5, 6}
# >>> 
# >>> A & A
# {1, 2, 3, 4}
# >>> 


# def printStarCircle(i=0,j=0):

# 	 while -10 < i :
# 	 	while j < 10:
# 	 		if i*i + j*j < 102:
# 	 			print("*", end="")
# 	 		else:
# 	 			print(" ", end="")
	 		
# 	 		i-=1
# 	 		j +=1
