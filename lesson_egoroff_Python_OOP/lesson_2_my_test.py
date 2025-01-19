import json
class Worker:
    def __init__(self):
        self.work1 = Zarplata()
        self.work2 = Zarplata()


class Zarplata:
    def __init__(self):
        self.zp = 600


x = Worker()

print(x.__dict__)   # объект класса воркер имеет в себе два атрибута которые являются объектами класса зарплата

print(x.work1.__dict__)
print(x.work2.__dict__)




