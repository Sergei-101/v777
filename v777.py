# Урок 13. Исключения
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения
# внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной
# длины.

class TestException(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Значения сторон должны быть положительными, а у Вас {self.a}, {self.b}, {self.c}"




def triangle(a:int, b:int, c:int):
    if a > 0 and b > 0 and c > 0:
        if a < b + c and b < a + c and c < a + b:
            if a == b == c:
                print("Треугольник равносторонний")
            elif a == b or b == c or c == a:
                print("Треугольник равнобедренный")
        else:
            print("Треугольник не существует")
    else:
        raise TestException(a, b, c)


triangle(11, 2, 3)




try:
    a = int(input("Введите число от 0 до 100 - "))
    b = []
    if a > 0 and a < 101:
        for i in range(1, a+1):
            if a % i == 0:
                b.append(i)
        if len(b) > 2:
            print(f"Число составное, число делится нацело на {b}")
        else:
            print("Число просте")
    else:
        print("Не выполнено условие")
except ValueError as e:
    print(f"Число должно быть написано цифрами ошибка {e}")