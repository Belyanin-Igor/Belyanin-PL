#Вариант 1, 1 номер
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = 0
y = 0

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i][j] > 0:
            x += A[i][j]
            y += 1

print("Сумма положительных элементов над главной диагональю:", x)
print("Количество положительных элементов над главной диагональю:", y)
