n = int(input("Введите натуральное число n (n ≤ 9): "))
if 1 <= n <= 9:
    for i in range(1, n + 1):
        print(''.join(str(x) for x in range(1, i + 1)))
else:
    print("Введите число от 1 до 9.")