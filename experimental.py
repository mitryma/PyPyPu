n=100
for x in range(2,n):
        if n % x ==0:
            print(n," " ,n/x)
            continue
else:
    print(n)

b=[]
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print (f(100,b),f(200,b))


def make_incrementor(n):
 return lambda x: x + n

ff=make_incrementor(42)
print(ff(0))
print(ff(1))

print("\n\n\n")


def fac(n):
    if n<= 1 : return 1
    return n*fac(n-1)

print(fac(3))

