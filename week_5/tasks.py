# 1.

# width = 17
# height = 12.0
# delimiter = '.'

# (a) width ---- 17
# (b) width / 2 ---- 8.5
# (c) width // 2 ---- 8
# (d) height // 7  ---- 1.0
# (e) 1 + 2 * 5  --- 11
# (f) delimiter * 5 ----  .....


# 2.

# a.
# >>> minutes = 3*60 +45
# >>> seconds = minutes *60 +2
# >>> seconds
# 13502

# b
# 3h   45m    2s

# total 6149s
# >>> totalSeconds = 6149
# >>> seconds = totalSeconds % 60
# >>> totalMinutes = totalSeconds // 60
# >>> minutes = totalMinutes
# >>> minutes
# 	102
# >>> hours = totalMinutes // 60
# >>> minutes = totalMinutes % 60
# >>> print(hours, minutes, seconds)
# 1 42 29
# >>> 

# 3.

# >>> math.sqrt(-6)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: math domain error
# >>> math.sqrt(6)
# 2.449489742783178
# >>> 


# 4.

# >>> math.sin(15)
# 0.6502878401571168
# >>> 63**2.5
# 31502.96086084608
# >>> math.sqrt(2498)
# 49.9799959983992
# >>> math.pi
# 3.141592653589793
# >>> 

# 5.

# >>> book = 24.95
# dicount = 0.4
# shipping = 3
# shipping_copy = 0.75
# >>> >>> >>> >>> 
# >>> dicount
# 0.4
# >>> discount = dicount
# >>> book_disc = book - book * discount
# >>> book_disc
# 14.969999999999999
# >>> book_disc = 14.97
# >>> total_books = book_disc * 60
# >>> total_price = total_books + shipping + shipping_copy *59
# >>> total_price
# 945.45
# >>> 


#6.

import time
import doctest

def hms(totalSeconds):
	seconds = totalSeconds % 60
	totalMinutes = totalSeconds // 60
	minutes = totalMinutes
	hours = totalMinutes // 60
	minutes = totalMinutes % 60
	delimiter = ':'
	print(hours,delimiter, minutes,delimiter, seconds)


# 7.
def total_seconds(hours,minutes,seconds):
	"""
>>> total_seconds(1,42,29)
6149

>>> total_seconds(0,0,29)
29

	"""

	total_minutes = hours * 60 + minutes
	total_seconds = total_minutes * 60 + seconds
	return total_seconds


# 9

# a = list(range(10))
# (a) a[2] -- 2
# (b) a[10] -- out of range
# (c) a[-3] -- 7 --- Goes from the end
# (d) a[0:3] -- 0,1,2
# (e) a[:3] -- 0,1,2 - up to 3 not including 3
# (f) a[4:] -- 4,5,6,7,8,9 -- including 4
# (g) a[:] -- 0 - 9
# (h) a[::2] -- 0,2,4,6,8 -- every 2
# (i) a[5::-1] -- 5,4,3,2,1,0 - goes backwards by 1
# (j) a[::2][3] -- goes every 2 -- 0,2,4,6,8. 
#					Selects number in position 3 -- 0=0, 2=1, 4=2, 6 = 3


# 10
# (a) a[4] to give 4
# (b) a[-5] to give 4 //// a[-6] not -5
# (c) a[0:2] to give [0, 1]
# (d) a[:3] to give [0, 1, 2]
# (e) a[-2:] to give [8, 9]
# (f) a[::3] to give [0, 3, 6, 9]
# (g) a[::-3] to give [9, 6, 3, 0]

# 11
# (a) All even numbers in a in ascending order. 
#a[::2]
# (b) The reverse of a
#a[::-1]
# (c) All odd numbers in a in descending order.
#a[9::-2]
# (d) The two highest odd numbers in a in descending order
#a[9:7:-1]


#extra
def print_characters():
	i = 0
	while i < 256:
		print(chr(i))
		print("")
		print(ord(chr(i)))
		print("")
		i += 1
		time.sleep(0.1)
def main():
	#
	return




if __name__ == "__main__":
    import doctest
    doctest.testmod()