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

def sigma((a,b),fn):
    return sum([fn(v) for v in range(a,b)])


def ident(n):
    return [[1.0 if i == j else 0.0 for j in range(0,n)] for i in range(0,n)]

def mmult(A,B):
    m,n = len(A),len(as_list(A[0]))
    m_,p = len(B),len(as_list(B[0]))
    return [
                [
                    sum([as_list(A[i])[k] * as_list(B[k])[j] for k in range(0,m)])
                    for j in range(0,p)
                ] for i in range(0,n) 
            ]
            
def fake_transpose(A):
    return sum(A,[])

def decompose(Ain):
    A = [row[:] for row in Ain]
    n = len(A)
    P = ident(n)

    # Pivot, one column at a time
    for pivot in range(0,n-1):
        # Find qmax in the pivot column
        qmax = max(range(pivot,n), key = lambda q: abs(A[q][pivot]))
        # Now swap
        P[qmax],P[pivot] = P[pivot],P[qmax]
        A[qmax],A[pivot] = A[pivot],A[qmax]

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
    print_mat("P",P)
    return A,P


def solve((LUin,P), bin):
    LU = [row[:] for row in LUin]
    n = len(LU)
    b = bin[:]
    b = mmult(P,b)
    print_mat("Pb",b)    
    b = fake_transpose(b)

    def forward_sub(L,n,b):
        y = [0] * n
        for i in range(0,n):
            y[i] = b[i] - sigma((0,i), lambda q: L[i][q]*b[q])
        print_mat("y",y)
        return y

    def backwards_sub(U,n,y):
        x = [0] * n
        for i in range(n-1,-1,-1):
            x[i] = (y[i] - sigma((i + 1,n), lambda q: U[i][q]*x[q]))/U[i][i]

        print_mat("x",x)
        return x

    return backwards_sub(LU,n,forward_sub(LU,n,b))

def genplu(A,b):
    return solve(decompose(A),b)

def test1():
    A = [
            [ 1.0, 0.0, 0.0, 0.0],
            [14.0, 0.0, 0.0,-2.0],
            [ 6.0, 0.0,-1.0, 0.0],
            [ 1.0, 2.0,-2.0,-1.0],
        ]
    b = [1.0,0.0,0.0,0.0] 
    print_mat("A",A)
    print_mat("b",b)
    genplu(A,b)

test1()
