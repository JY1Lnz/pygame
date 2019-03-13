class Student(object):

    def __init__(self, name, score):
        self.__name = name  # 变量名前加双下划线表示私有变量
        self.__score = score

    def print_score(self):
        print('%s: %d' % (self.__name, self.__score))

    def print_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


class Animal(object):

    def run(self):
        print("Animal is running...")


class Dog(Animal):

    def run(self):
        print("Dog is running...")


class Cat(Animal):

    def run(self):
        print("Cat is running...")


bart = Student('Bart Simpson', 59)

while True:
    for i in range(10):
        exit()
