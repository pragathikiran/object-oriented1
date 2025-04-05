class student:

 grade = 10

 name = "pragathi"

 age = 15


def introduction(self):

 print("Hi I am a student")

def details(self):

 print("My name is", self.name)

 print("I study in Grade", self.grade)

 print("I am", self.age, "years old")

ob = student()

ob.introduction()

ob.details()