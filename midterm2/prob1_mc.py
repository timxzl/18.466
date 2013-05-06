import random as rr

def mle_error(x1, x2, x3, N):
    if x1<x2:
        x1 = x2
    if x1<x3:
        x1 = x3
    return x1-N

def mle_sample(N):
    return mle_error(rr.randint(1,N), rr.randint(1,N), rr.randint(1,N), N)**2

def mle_simulate(N, M):
    sum = 0
    for i in xrange(M):
        sum += mle_sample(N)
    return sum / float(M)


def mle_sum(N):
    sum = 0
    for x in xrange(1-N, 0):
        sum += x**2*(3*x**2 + 3*(2*N-1)*x + (3*N**2-3*N+1))
    return sum/float(N**3)

def mom_error(x1, x2, x3, N):
    return (x1+x2+x3)*2/3.0-1-N

def mom_simulate(N, M):
    sum = 0
    for x in xrange(M):
        sum += mom_error(rr.randint(1,N), rr.randint(1,N), rr.randint(1,N), N)**2
    return sum/float(M)

def mom_eq(N):
    return (N**2-1)/9.0

def mom_minus_mle(N):
    return (mom_eq(N)-mle_sum(N))*180*(N**2)/float(N-1)

def mom_minus_mle_eq(N):
    return 2*N**3+47*N**2-33*N+12

def NRB_sq_sum(N):
    sum = 0
    for m in xrange(1, N+1):
        sum += (4*(m**3)-6*(m**2)+4*m-1)**2/float(3*(m**2)-3*m+3/4.0)
    return sum

def NRB_sq_eq(N):
    return 4*N*(4*(N**4)+1)/15.0

def comp_error(N):
    mom = (N**2-1)/9.0
    mom_app = (N**2)/9.0
    mle = (N-1)*(2*N-1)*(3*(N**2)-3*N+4)/float(60*(N**2))
    mle_app = (N**2)/10.0
    rb = (N**4+4)/(15.0*(N**2))
    rb_app = (N**2)/15.0
    return (mom, mom_app, mle, mle_app, rb, rb_app)
