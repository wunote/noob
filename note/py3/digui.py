
def dg(num):
    if num == 1:
	    return num
    else:
	    return num * dg(num-1)

print(dg(10))

def hanoi(n, x, y, z):
    if n == 1:
	    print(x, '--->', z)
    else:
	    hanoi(n-1, x, z, y)
	    print(x, '--->', z)
	    hanoi(n-1, y, x, z)

hanoi(4, "X", "Y", "Z")
