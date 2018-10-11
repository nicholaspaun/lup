def as_list(v):
    if type(v) == list: return v
    return [v]

def print_mat(name, mat):
    print "\n%s = " % (name)

    for row in mat:
        for col in as_list(row):
            print "% 8.3f" % (col) +  "\t\t",
        print "\n",


def sigma((a,b), valS, fn):
    valS = [val[a:b] for val in valS]
    return sum([fn(v) for v in zip(*valS)])



def decompose(Ain):
    A = [row[:] for row in Ain]
    n = len(A)

    # Pivot, one column at a time
    for pivot in range(0,n-1):
        # For every row below the one which contains the pivot element
        for i in range(pivot + 1, n):
            # Lower part of A is all zeros -- stuff in the m coefficients which can be used to reduce b
            m = A[i][pivot] / A[pivot][pivot]
            A[i][pivot] = m
            # Upper part of A stores U, actually the results of running the algorithm
            for j in range(pivot + 1, n):
                A[i][j] -= m*A[pivot][j]
                     
    print ""
    print_mat("A = LU", A)
    return A


def solve(LUin, bin):
    LU = [row[:] for row in LUin]
    n = len(LU)
    b = bin[:]
    assert n == len(b)

    def forward_sub(L,n,b):
        y = [0] * n
        for i in range(0,n):
            y[i] = b[i] - sigma((0,i),[L[i],b], lambda (Li,bi): Li * bi)
        print_mat("y",y)
        return y

    def backwards_sub(U,n,y):
        x = [0] * n
        for i in range(n-1,-1,-1):
            x[i] = (y[i] - sigma((i + 1,n),[U[i],x], lambda (Ui,xi): Ui * xi))/U[i][i]

        print_mat("x",x)
        return x

    return backwards_sub(LU,n,forward_sub(LU,n,b))

def genplu(A,b):
    return solve(decompose(A),b)

def test1():
    A = [
            [14.0, 0.0, 0.0,-2.0],
            [ 1.0, 2.0,-2.0,-1.0],
            [ 6.0, 0.0,-1.0, 0.0],
            [ 1.0, 0.0, 0.0, 0.0]
        ]
    b = [0.0,0.0,0.0,1.0] 
    print_mat("A",A)
    print_mat("b",b)
    genplu(A,b)

test1()
