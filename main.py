# noinspection PyUnreachableCode
class Student:
    def __init__(self, name, surname, age, group, money, money1, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.money = money
        self.money1 = money1
        self.marks = marks

    def info(self):
        print(f"Student {self.name} {self.surname}")



    def dx(self):
        self.money = float(input("start money:"))
        if (self.money) < 500:
                print("You lose")
        elif (self.money) > 1000:
            print("good")
        else:
            print("Ти можеш навчатися і заробляти гроші забажанням")
        print(f'money = {self.money}')
    def year(self):
        self.money1 = float(input("your salary:"))
        print(f'money = {self.money + self.money1 * 12 - 7565}')
        if (self.money + self.money * 12) > 12000:
            print("yay you not loser :)")
        else:
            print("you loser")
    def learn(self):
        global money
        if 7 >= sum(self.marks) / len(self.marks) :
            int(self.money-750*12)
            return sum(self.marks) + 6
        elif 4 >= sum(self.marks) / len(self.marks) :
            self.money-750*12
            return sum(self.marks) / len(self.marks) + 6
    def average(self):
        return sum(self.marks) / len(self.marks)
student1 = Student(
    "Vlad",
    "Gesshin",
    27,
    "Hg17",
    0,
    0,
    [4, 4, 5, 6,7 ],
)
student2 = Student(
    "Valentin",
    "Bobyk",
    23,
    "HG13",
    0,
    0,
    [10, 12, 11, 7, 1, 3, 9, 7, 6, 8, 12, 12, 10],

)
student1.info()
student1.dx()
student1.learn()
student1.year()
print(student1.average())
student2.info()
student2.dx()
student2.learn()
student2.year()
student2.dx()
print(student2.average())