# Tower of Hanoi solver showing the importance of recursion 
# A, B, C representing the three towers. 
# Assuming all discs are in A towers the code below gives 
#instructions to a robot to move disc from one tower to another. 
#m representing the number of discs in the intial tower (tower A)

def move(a,f):
	print("Move the disc from {} to {}".format(a, f))


def hanoi_solver(m,a,y,f):
	if m==0:
		pass
	else:
		hanoi_solver(m-1,a,f,y)
		move(a,f)
		hanoi_solver(m-1,y,a,f)

hanoi_solver(6, "A", "B", "C")


