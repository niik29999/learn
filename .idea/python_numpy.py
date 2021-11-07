import numpy as np

my_list = [1, 2, 5, 1, 7, 9]
arr = np.array(my_list)
print(arr)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_matrix))
print(np.arange(25))
print(np.arange(0,15,3))
print(np.zeros(3))
print(np.zeros((3,3)))
print(np.ones((3,3)))

# матрица с заданным размером с числами в заданном диапазоне
print(np.linspace(0,10,5))
print(np.linspace(2,14,13))
print(np.linspace(2,14,50))


print(np.eye(4))

# матрица со случайным набором чисел, с заданным размером
print(np.random.rand(2))
print(np.random.rand(2,2))
print(np.random.randn(2))
print(np.random.randn(5,5))

# случайное число из диапазона
print(np.random.randint(1,100))
# заданое количество случайных чиел из диапазона
ranarr = np.random.randint(1,100,10)
print(ranarr)

# разделение списка по строкам и полям
arr = np.arange(25)
print(arr)
arr = arr.reshape(5,5)
print(arr)
print(arr.shape)
print(arr.reshape(1,25))
print(arr.reshape(25,1))
arr = np.arange(25).reshape(5,5)
print(arr)

# max,min,argmax,argmin
print(ranarr)
print(ranarr.max())
print(ranarr.argmax())

# типы объектов в списке
print(ranarr.dtype)

# выводим часть массива
arr = np.arange(12)
print(arr[:5])
arr = arr.reshape(4,3)
print(arr)
print(arr[:2,1:])
arr = np.arange(12)

# проверка всех элементов списка на условие
bool_arr = arr > 7
print(bool_arr)
print(arr[bool_arr])
print(arr[arr > 7])

# операции с массивами (полный список в документации)
arr = arr.reshape(4,3)
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr + 5)
print(arr.max())
print(arr.sum())
print(arr.sum(axis=0))
# print(1 / arr)
print(np.sqrt(arr))


