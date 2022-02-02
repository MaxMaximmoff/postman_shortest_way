# -*- coding: utf-8 -*-
# Решение задачи маршрута почтальона методом перебора

# функция вычисления расстояния между двумя точками
def distance(point_1, point_2):
    d = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    return d

# Создание массива с расстояниями между точками            
def distances(points):
    mas = [[]]
    mas = [[distance(points[j], points[i]) for j in range(len(points))] for i in range(len(points))]
    return mas
      
# координаты точек
p_1 = (0, 2)  # Почтовое отделение
p_2 = (2, 5)  # Ул. Грибоедова, 104/25
p_3 = (5, 2)  # Ул. Бейкер стрит, 221б
p_4 = (6, 6)  # Ул. Большая Садовая, 302-бис
p_5 = (8, 3)  # Вечнозелёная Аллея, 742

# массив с координатами точек
points = [p_1, p_2, p_3, p_4, p_5]
# подстановка значений в формулу

# заполнение массива с путями между точками
distances = distances(points)

# массив, где будут храниться все просчитанные маршруты
path = []

# порядковый номер текущего маршрута
counter = 0

# самый короткий путь (изначально ставим заведомо большим)
minPath = 10000;

# номер самого короткого маршрута
minCounter = 0

# индкс начальной точки пути почтальона
i1 = 0;

# перебираем все варианты перемещения по точкам
for i2 in range(len(points)): 
    for i3 in range(len(points)):
        for i4 in range(len(points)):
            for i5 in range(len(points)):
                # условие непосещение одной и той же точки два раза
                if ((i1!=i2)and(i1!=i3)and(i1!=i4)and(i1!=i5)and(i2!=i3)and(i2!=i4)and(i2!=i5)and(i3!=i4)and(i3!=i5)and(i4 != i5)):
                    # запоминаем текущий путь
                    path.insert(counter, 'p_{} → p_{} → p_{} → p_{} → p_{} → p_{}'.format(i1+1, i2+1, i3+1, i4+1, i5+1, i1+1))
                    print(path[counter])
                    # ищем минимальный путь путь
                    if ( (distances[i1][i2] + distances[i2][i3] + distances[i3][i4] + distances[i4][i5] + distances[i5][i1]) < minPath) :
                        minPath = distances[i1][i2] + distances[i2][i3] + distances[i3][i4] + distances[i4][i5] + distances[i5][i1]
                        print(minPath)
                        minCounter = counter;
                    counter +=1
                    
# Вывод результата
print('Координаты точек маршрута почтальона:')
print('p_1 = (0, 2)  # Почтовое отделение')
print('p_2 = (2, 5)  # Ул. Грибоедова, 104/25')
print('p_3 = (5, 2)  # Ул. Бейкер стрит, 221б')
print('p_4 = (6, 6)  # Ул. Большая Садовая, 302-бис')
print('p_5 = (8, 3)  # Вечнозелёная Аллея, 742')
print('')
print('Оптимальный маршрут: {} расстояние = {}'.format(path[minCounter], minPath))
