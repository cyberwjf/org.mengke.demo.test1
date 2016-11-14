def move(x, a, b, c):
    if x == 1:
        print a + " -> " + c
    else:
        move(x-1, a, c, b)
        print a + " -> " + c
        move(x-1, b, a, c)

def hano(x):
    print "hano(" + str(x) + "):"
    move(x, 'a', 'b', 'c')

if __name__ == "__main__":
	hano(4)

