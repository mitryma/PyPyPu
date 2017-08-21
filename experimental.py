'''
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
'''

c = [c * 4 for c in 'list']
print(c)
print(c.count("llll"))
c.append(1)
print(c)
d=c.copy()
print(d)
c.extend(c)
print(c)
c.append(3)
print(c.index("ssss",1,8)," " ,c.count("tttt")," ",c.count(3) )
print(c)
c.reverse()
print(c)
#c.sort()
#print(c)

dd=dict()
#dd=dd+{[1,1]}
dd=dict([(1, 1), (2, 4)])
dd.update([(3,2)])
dd.update([('dict',1), ('dictionary',2)])
print(dd," ",type(dd)," ")
pp=dd.get('dict')
print(pp)
print(dd.items())
print(dd.keys())

