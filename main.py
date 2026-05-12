import numpy as np

# Створення масиву

array = np.random.randint(-100, 101, size=200)

print("\n 1. Початковий масив")
print(f"Початковий масив: \n {array}")
print(f"Розмір масиву: {array.size}")
print(f"Мін: {array.min()} | Макс: {array.max()}")

# Фільтрація додатних чисел через маску
positive_mask = array > 0          
positive_numbers = array[positive_mask]   

print("\n 2. Додатні числа через маску")
print(f"Кількість додатних чисел: \n {positive_numbers.size}")
print(f"Додатні числа: {positive_numbers}")

# Заміна від'ємних значень на нулі
array_no_negative = array.copy()        
negative_mask = array_no_negative < 0   
array_no_negative[negative_mask] = 0    

print("\n 3. Масив після заміни від'ємних на нулі")
print(f"Масив : \n {array_no_negative}")
print(f"Кількість нулів у масиві: {np.sum(array_no_negative == 0)}")
print(f"Від'ємних чисел залишилось: {np.sum(array_no_negative < 0)}")

# Середнє значення
mean_value = np.mean(array_no_negative)

print("\n 4. Середнє значення")
print(f"Середнє значення масиву: {mean_value:.2f}")


print("\n ПІДСУМОК")
print(f"  Розмір початкового масиву : {array.size}")
print(f"  Кількість додатних чисел  : {positive_numbers.size}")
print(f"  Кількість від'ємних чисел : {np.sum(array < 0)}")
print(f"  Кількість нулів (було)    : {np.sum(array == 0)}")
print(f"  Середнє після обробки     : {mean_value:.2f}")

