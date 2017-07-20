


def multiply(a,b):

	bigger = max(a,b)
	smaller = min(a,b)
	return multiplyHelper(a,b)

def multiplyHelper(smaller,bigger):
	
	if smaller == 0:
		return 0
	elif smaller == 1:
		return bigger
	
	s = smaller >> 1 #Divide by 2
	side1 = multiplyHelper(s,bigger)
	side2 = side1

	if smaller%2 == 1:
		side2 = multiplyHelper(smaller - s, bigger)
	return side1 + side2

def multiply_cached(a,b):
	
	bigger = max(a,b)
	smaller = min(a,b)
	cache = [0]*(smaller + 1)
	return multiply_cached_helper(a,b,cache)

def multiply_cached_helper(smaller,bigger,cache):
	
	if smaller == 0:
		return 0
	elif smaller == 1:
		return bigger
	elif cache[smaller] > 0:
		return cache[smaller]
	
	s = smaller >> 1
	side1 = multiply_cached_helper(s,bigger,cache)
	side2 = side1

	if smaller%2 ==1:
		side2 = multiply_cached_helper(smaller -s, bigger, cache)
	cache[smaller] = side1 + side2
	return cache[smaller]

print(multiply(17,22))
print(multiply_cached(17,22))

