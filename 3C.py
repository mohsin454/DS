def add(x, y, a, b): 
	size = max(a, b); 
	sum = [0 for i in range(size)] 	
	for i in range(0, a, 1): 
		sum[i] = x[i] 
	for i in range(b): 
		sum[i] += y[i] 
	return sum

def printPoly(poly, b): 
	for i in range(b): 
		print(poly[i], end = "") 
		if (i != 0): 
			print("x^", i, end = "") 
		if (i != b - 1): 
			print(" + ", end = "")
			
if __name__ == '__main__': 		
	x = [4, 0, 4, 2] 	
	y = [3, 4, 3] 
	a = len(x) 
	b = len(y) 
	print("First polynomial is") 
	printPoly(x, a) 
	print("\n", end = "") 
	print("Second polynomial is") 
	printPoly(y, b) 
	print("\n", end = "") 
	sum = add(x, y, a, b) 
	size = max(a, b) 

	print("sum polynomial is") 
	printPoly(sum, size) 
