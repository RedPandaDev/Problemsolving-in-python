# def rectangle(m=5, n=10):
# 	i = 0
# 	b = 0
# 	a = 2

# 	while b != m:
# 		print()
# 		b += 1
# 		i = 0
# 		while i != n:
			
# 			if a < 3:
# 				print("* ", end="")
# 				i+=1
# 				a+=1
# 			elif a < 7:
# 				print("_ ", end="")
# 				i+=1
# 				a+=1
# 			if a == 6:
# 				a = 0
# 	return


# def press_button(lights = 50, press = 0):
#     lightsarray = [False] * lights # All lights are off at start
#     	# press +1 because error with slice 0 so had to move it all up by 1
#     i = 1
#     while press+1 > i:
#     	change = i +1
#     	lightsarray[::change] = [not y for y in lightsarray[::change]]
#     	print(change)
#     	i += 1	

#     return lightsarray

# def press_button(lights = 50, press = 0):
#     lightsarray = [False] * lights # All lights are off at start
#     	# press +1 because error with slice 0 so had to move it all up by 1

#     press_number = 1
#     change = 0

#     while press_number < press:

#     	while change < lights:


#     		if lightsarray[change] == False:
#     			lightsarray[change] = True
#     		else:
#     			lightsarray[change] = False

#     		change += press_number

#     	press_number += 1
#     	change = 0


#     return lightsarray

# def press_button(n):
#     lightsarray = [False] * 50 ### All lights are off at start ###
#     press = 1
#     while press < n +1: 
#     	for change in range(1, press + 1):   
#         	lightsarray[::change] = [not y for y in lightsarray[::change]]
#     	press += 1

#     return lightsarray


# def press_button(n):
# 	lightsarray = [False] * 50 ### All lights are off at start ###


# 	lightsarray[::n] = [not y for y in lightsarray[::n]]# this shit works


def press_button(n):
	lightsarray = [False] * 50 ### All lights are off at start ###

	light = 1

	 # this shit works with n and no light

	while light != n +1:
		lightsarray[::-light] = [not y for y in lightsarray[::-light]]
#		print(light)
		light +=1
		lightsarray.reverse()

#lightsarray[::-n] = [not y for y in lightsarray[::-n]]
# ----- this shit is correct but backwards :o
#  So flip the freaking arrray when returning
    
	return lightsarray