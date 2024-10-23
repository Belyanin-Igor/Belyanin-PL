N = int(input("Введите количество элементов в массиве: "))
array = []
print("Введите элементы массива:")
for i in range(N):
    element = float(input(f"Элемент {i + 1}: "))
    array.append(element)
min_abs_element = min(array, key=abs)
print(f"Минимальный по модулю элемент: {min_abs_element}")
print("Массив в обратном порядке:")
print(array[::-1])