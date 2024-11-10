numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
mis = 4
s = sum(numbers[:mis]) + sum(numbers[mis+1:])
count = len(numbers)
ave = s/count
numbers[4] = ave
print("Измененный список:", numbers)
