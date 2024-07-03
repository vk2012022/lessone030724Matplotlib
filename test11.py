import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 5  # Количество образцов

# 1 массив из 5 случайных чисел
random_array_x = np.random.rand(num_samples)
print(random_array_x)
# 2 массив из 5 случайных чисел
random_array_y = np.random.rand(num_samples)
print(random_array_y)

x = random_array_x
y = random_array_y

# Создание диаграммы рассеяния
plt.scatter(x, y)

# Добавление заголовка и подписей к осям
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')

# Отображение графика
plt.show()
