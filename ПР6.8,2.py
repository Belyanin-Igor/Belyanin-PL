array = [1.0, 2.0, 0.0, 4.0, 0.0, 6.0]
non_zero_elements = [x for x in array if x != 0]
mean_value = sum(non_zero_elements) / len(non_zero_elements) if non_zero_elements else 0
array = [mean_value if x == 0 else x for x in array]
print("Измененный массив:", array)