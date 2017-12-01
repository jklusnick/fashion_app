def add(a, b):
	return a + b

def sub(a, b, c=0, d=0, e=0):
	return a - b - c - d - e

def div(a, b):
	return a / b

def mult(a, b):
	return a * b

print (add(13, add(8, add(5, add(3, add(2, add(1, 1)))))))

print (sub(1, 1, 3, 5, 6))

print (add(sub(add(100, 100), 200), 350))

print (div(100, 10))

print (add(div(100, 10), div(mult(20, 2), 4)))

print (div(div(100, 10), 10))

print (add(mult(mult(mult(mult(2, 2), 2), 2), 2), 64))