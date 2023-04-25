from person.person import Person, Student

my_person = Person("Tanya", 35, "Moscow", "Russian", "Female")
my_person.introduce_yourself()
print("\n")
my_person.age_person()
print("Next year my age will be:", my_person.age)
print("\n")
my_student = Student("Tanya", 35, "Moscow", "Russian", "Female", "Moscow State University of Civil Engineering", 2010, 4, "Economics of Enterprises and Organizations in Investment and Construction Field")
my_student.info_about_student()