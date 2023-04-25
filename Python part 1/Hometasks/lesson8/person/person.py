
class Person():
    def __init__(self, name, age, place_of_birth, nationality="Russian", sex="Male"):
        self.name = name
        self.age = age
        self.place_of_birth = place_of_birth
        self.nationality = nationality
        self.sex = sex

    def introduce_yourself(self):
        print(f"My name is {self.name}.")
        print(f'I am {self.age} years old.')
        print(f'I was born in {self.place_of_birth}.')
        print(f'My nationality is {self.nationality}.')
        print(f'My gender is {self.sex}.')

    def age_person(self):
        self.age += 1

class Student(Person):

    def __init__(self, name, age, place_of_birth, nationality, sex, university, year_of_graduation, average_score, profession):
        super().__init__(name, age, place_of_birth, nationality, sex)
        self.university = university
        self.year_of_graduation = year_of_graduation
        self.average_score = average_score
        self.profession = profession

    def info_about_student(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        print(f"I studied at {self.university}.")
        print(f"My profession is {self.profession}.")
        print(f"I graduated from the {self.university} in {self.year_of_graduation} with an average score {self.average_score}.")
