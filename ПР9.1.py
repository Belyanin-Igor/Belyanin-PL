def f (num1):
    if num1==1:
        return 1
    else:
        return num1*f(num1-1) 
x = int(input('x: '))
n = int(input('n: '))
b = (x**n)/f(n)
print('Ответ: ', b)