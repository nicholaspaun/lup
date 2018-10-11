#A = [[6.0,0.0,-1.0,0.0],[14.0,0.0,0.0,-2.0],[1.0,2.0,-2.0,-1.0],[1.0,0.0,0,0]]
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
L = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
U = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]

def printmat(X):
    for row in X:
        for col in row:
            print "% 7.3f" % col + "\t\t\t",
        print "\n",
    print "\n",
    

for j in range(0,n):
    L[j][j] = 1.0

for leader in range(0,m-1):
    for row in range(int(leader+1),n):
        M = A[row][leader]/A[leader][leader]
        L[row][leader] = M
        for col in range(int(leader),m):
                A[row][col] = A[row][col] - M*A[leader][col]


y = [0,0,0,0]
for i in range(0,n):
    y[i] = b[i] - sum([li*yi for li,yi in zip(L[i][0:i],y[0:i])])
print y
x = [0,0,0,0]
x[n-1] = y[n-1]/A[n-1][n-1]
for i in range(n-2,-1,-1):
    print i
    x[i] = (y[i] - sum([ui*xi for ui,xi in zip(A[i][i+1:n],x[i+1:n])])) / A[i][i]

print x
printmat(L)
print b
printmat(A)

