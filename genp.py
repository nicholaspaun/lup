#A = [[6.0,0.0,-1.0,0.0],[-14.0,0.0,0.0,-2.0],[1.0,2.0,-2.0,-1.0],[1.0,0.0,0,0]]
#b = [0.0,0.0,0.0,1.0]

A = [
        [6.0,-2.0,2.0,4.0],
        [12.0,-8.0,6.0,10.0],
        [3.0,-13.0,9.0,3.0],
        [-6.0,4.0,1.0,-18.0]
    ]
b = [16.0,26.0,-19.0,-34.0]

m = len(A)
n = len(A[0])

for leader in range(0,m-1):
    for row in range(int(leader+1),n):
        M = A[row][leader]/A[leader][leader]
        for col in range(int(leader),m):
            A[row][col] -= M*A[leader][col]
        
        b[row] -= M*b[leader]

x = [0,0,0,0]
x[n-1] = b[n-1]/A[n-1][n-1]
for row in range(n,-1,-1):
    x[row] = (b[row] - sum([ap*xp for ap,xp in zip(A[row][row + 1:n],x[row + 1:n])])) / A[row][row]

print x
print A,b
            

