from c3 import Human


class Student(Human):
    # 类变量，为所有实例共享特征值
    name = '123'
    age = 0

    def __init__(self, name, age):
        # 构造函数
        # 构造函数自动调用
        # 初始化对象的属性
        # 使用self保存实例变量
        # self.name = name
        # self.age = age
        # self.score = 0
        # self.__serr = 'ffff'
        # print(Student.name)  # 实例中访问类变量1
        # self.__class__.age += 1
        super(Student, self).__init__(name, age)
        # print(self.__class__.name)  # 实例中访问类变量2
        # print(self)
        # print(name, age)

    def __marking(self, score):
        if score < 0:
            return '请输入分数大于等于0或小于等于100'
        elif score > 100:
            return '请输入分数大于等于0或小于等于100'
        else:
            self.score = score
            print('分数为%g' % self.score)
            print(self.age)

    def do_homework(self):
        print('homework')

    @classmethod
    def plus_sum(cls):
        cls.name = '你好'
        print(cls.name)

    @staticmethod  # 静态方法尽可能少用
    def add(x, y):
        print(Student.name)
        print('This is staticmethod')


student1 = Student('石敢当', 18)
print(student1.name)
print(student1.age)
# student2 = Student('石敢当', 18)
# Student.plus_sum()
# student1.add(1,2)
# student1.plus_sum()  # 实例可以调用类方法，但不建议这样做
# Student.add(1, 2)
