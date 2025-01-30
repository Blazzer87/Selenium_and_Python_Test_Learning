"""задачка 1 с метанита
Определите класс Rectangle, который представляет прямоугольник. Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах width и length соответственно.
Также этом классе определите метод area, который возвращает площадь прямоугольника, и метод perimeter, который возвращает периметра прямоугольника.
После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов."""

class Rectangle:

    def __init__(self, width ,length ):
        self.width = width
        self.length = length

    def area(self):
        print(self.width * self.length)

    def perimeter(self):
        print((self.width + self.length) * 2)


object1 = Rectangle(5,10)

object1.area()
object1.perimeter()

