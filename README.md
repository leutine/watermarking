# Watermarking Project 
Модули:
0. Основной 

1. Предобработка
    1. Ввод изображения.
    Принимает: изображение по стандартному пути (img/orig/*.png)
    Возвращает: массив яркостей пикселей размером равным размеру изображения
    
    2. Разеделение изображения на блоки.
    Принимает: массив яркостей пикселей изображения
    Возвращает: массив массивов размером 8х8
    
    3. Генерация вкладываемого сообщения
    
2. Вложение
    1. Прямое ЦВПХ (Целочисленное Вейвлет-Преобразование Хаара).
    Принимает: массив яркостей пикселей
    Возвращает: массив низкочастотных значений, массив высокочастотных значений
    
    2. Проверка свойства расширяемости
    
    3. Проверка свойства изменяемости
    
    4. Расчет ключа для вложения
    
    5. Вложение в расширяемые биты
    
    6. Обратное ЦВПХ
    
3. Извлечение

4. Постобработка
    1. Объединение блоков изображения.
    Принимает: массив массивов размером 8х8 
    Возвращает: массив яркостей пикселей изображения
    
    2. Вывод изображения в файл.
    Принимает: массив яркостей пикселей изображения
    Возвращает: изображение по стандартному пути (img/wm/*_wm.png)
    
5. Построение графиков  
    1. Вывод изображений (до и после) на экран.
    
    2. Построение вспомогательных графиков.
    
    
6. Расчет схожести
