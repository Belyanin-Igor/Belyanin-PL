def f(a,b):
    if a>b:
        print(b)
        return f(a,b+1)
    if a<b:
        print(b)
        return f(a,b-1)
    if a==b:
        return b
c=int(input())
d=int(input())
print(f(c,d))