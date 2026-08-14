from person import Person
from student import Student


p = Person()

p.name = "Mark"
p.age = 30

print(p.name, p.age)
print(p._generate_random_first_name())
print(p.retrieve_random_name())
print(Person._generate_random_first_name_kana())


s = Student()

s.name = "John"
s.age = 19
s.course = "BSIT Maj. GameDev"
s.year_level = 4

print(s.name)
print(s.age)
print(s.course)
print(s.year_level)
